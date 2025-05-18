CREATE DATABASE employee_db;

use employee_db;
-- roles
CREATE TABLE role (
    role_id INT PRIMARY KEY AUTO_INCREMENT,
    role VARCHAR(100) UNIQUE
);

-- locations
CREATE TABLE locations (
    location_id INT PRIMARY KEY AUTO_INCREMENT,
    location_name VARCHAR(100) UNIQUE
);

-- employees
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    role_id INT,
    location_id INT,
    experience DECIMAL(5,2),
    compensation DECIMAL(12,2),
    status VARCHAR(10),
    last_working_day DATE,
    FOREIGN KEY (role_id) REFERENCES role(role_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);
