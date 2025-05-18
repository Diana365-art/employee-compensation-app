import pandas as pd
import mysql.connector
from datetime import datetime

# Load cleaned CSV
df = pd.read_csv('C:\\Users\\DIANA\\OneDrive\\Desktop\\employee-compensation-app\\backend\\cleaned_employee_data.csv')


# Drop extra unnamed columns if any
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Normalize missing values to None
df = df.replace({pd.NA: None, pd.NaT: None, float('nan'): None, 'nan': None, 'NaN': None, '': None})
df = df.where(pd.notnull(df), None)

# Establish DB connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="emp_forecast"
)
cursor = conn.cursor()

# --- Insert unique roles ---
roles = df['role'].dropna().unique()
role_map = {}
for role in roles:
    cursor.execute("INSERT IGNORE INTO role (role) VALUES (%s)", (role,))
    conn.commit()
    cursor.execute("SELECT role_id FROM role WHERE role = %s", (role,))
    role_map[role] = cursor.fetchone()[0]

# --- Insert unique locations ---
locations = df['location'].dropna().unique()
loc_map = {}
for loc in locations:
    cursor.execute("INSERT IGNORE INTO locations (location_name) VALUES (%s)", (loc,))
    conn.commit()
    cursor.execute("SELECT location_id FROM locations WHERE location_name = %s", (loc,))
    loc_map[loc] = cursor.fetchone()[0]

# --- Insert employee data ---
for idx, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO employees (name, role_id, location_id, experience, compensation, last_working_day)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row['name'],
            role_map.get(row['role']),
            loc_map.get(row['location']),
            float(row['experience']) if row['experience'] is not None else None,
            float(row['compensation']) if row['compensation'] is not None else None,
            pd.to_datetime(row['last_working_day']).date() if row['last_working_day'] else None
        ))
    except Exception as e:
        print(f"\n[Error at row {idx}] {row.to_dict()}")
        print("Exception:", e)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Data import complete.")
