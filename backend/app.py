from flask import Flask, request, jsonify, render_template
import mysql.connector
import os
from dotenv import load_dotenv
from flask_cors import CORS
from flask import send_file

from io import StringIO, BytesIO
import csv
from flask import send_file

app = Flask(__name__)
CORS(app)
load_dotenv()

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/api/employees', methods=['GET'])
def get_employees():
    role = request.args.get('role')
    location = request.args.get('location')
    include_inactive = request.args.get('include_inactive') == 'true'
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("FilterEmployees", [role, location, include_inactive])
    for result in cursor.stored_results():
        employees = result.fetchall()
    cursor.close()
    conn.close()
    return jsonify(employees)

@app.route('/api/download-csv', methods=['GET'])
def download_csv():
    role = request.args.get('role', '')
    location = request.args.get('location', '')
    include_inactive = request.args.get('include_inactive') == 'true'

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("FilterEmployees", [role, location, include_inactive])
    for result in cursor.stored_results():
        rows = result.fetchall()

    
    string_io = StringIO()
    writer = csv.writer(string_io)
    writer.writerow(['Name', 'Role', 'Location', 'Experience', 'Compensation', 'Status'])

    for row in rows:
        writer.writerow([
            row['name'],
            row['role'],
            row['location_name'],
            row['experience'],
            row['compensation'],
            row['status']
        ])

    
    mem = BytesIO()
    mem.write(string_io.getvalue().encode('utf-8'))
    mem.seek(0)

    return send_file(
        mem,
        mimetype='text/csv',
        as_attachment=True,
        download_name='filtered_employees.csv'
    )



@app.route('/api/simulate-increment', methods=['POST'])
def simulate_increment():
    data = request.json
    percent = float(data['percent'])
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("SimulateGlobalIncrement", [percent])
    for result in cursor.stored_results():
        data = result.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/api/experience-distribution', methods=['GET'])
def experience_group():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.callproc("GroupByExperience")
    for result in cursor.stored_results():
        data = result.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
