#  Employee Compensation Forecasting Application

A full-stack web dashboard for filtering employee data, simulating global compensation increments, and analyzing workforce experience distribution.

---

##  Features

- Filter employees by role, location, and active status.
- Simulate global compensation increments.
- View experience-based employee distribution (0–1, 1–2, 2–5, 5+ years).
- Backend powered by Flask and MySQL.
- Frontend built using HTML, CSS, and JavaScript 

---

##  Tools and Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Libraries:** Flask-CORS, python-dotenv, mysql-connector-python
- **Other:** GitHub, VS Code
  
---------------------------------
- Setup Instructions

### Prerequisites

- Python 3.x
- MySQL Server
- Vs code studio
- Git
- pip (Python package manager)


---
### Project Structure
employee-compensation-forecast/
│
├── app.py                         # Flask backend
├── requirements.txt               # Python dependencies
├── templates/
│   └── index.html                 # Main HTML file
├── static/
│   ├── styles.css                 # CSS for styling
│   └── script.js                  # JS for dynamic content and API calls
├── sql/
│   ├── schema.sql          # SQL to create tables
│   └── stored_procedures.sql      # All required stored procedures
├── .env                
├── README.md                      # Full project documentation
└── screenshots/                   
    └── picture.png

##Set up virtual environment and install dependencies:
pip install -r requirements.txt

### Configure Environment Variables:
Create a .env file:
DB_HOST=localhost
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_NAME=employee_db

#### Set up the MySQL Database:

Run the SQL table creation script
Execute stored_procedures.sql to create:
FilterEmployees
GroupByExperience
SimulateGlobalIncrement

### Run the Flask app
python app.py

#### User Stories Fulfilled
User Story 1: Filter and Display Active Employees by Role
Filters employees by Role and Location
Toggles Active/Inactive employees
Displays:
Name
Role
Location
Compensation
Status

User Story 2: Group Employees by Years of Experience
Shows employee count grouped by:

0–1 years

1–2 years

2–5 years

5+ years

User Story 3: Simulate Compensation Increments
Enter a global % increment (e.g. 10%)

View:
Current vs. Updated Compensation

User Story 4: Download Filtered Employee Data
Exports to CSV:

Name
Role
Location
Experience
Compensation
Status





