DELIMITER $$

CREATE PROCEDURE FilterEmployees (
    IN in_role VARCHAR(100),
    IN in_location VARCHAR(100),
    IN in_include_inactive BOOLEAN
)
BEGIN
    SELECT e.name, r.role, l.location_name, e.experience, e.compensation, e.status
    FROM employees e
    JOIN role r ON e.role_id = r.role_id
    JOIN locations l ON e.location_id = l.location_id
    WHERE (in_role IS NULL OR r.role = in_role)
      AND (in_location IS NULL OR l.location_name = in_location)
      AND (in_include_inactive OR e.status = 'Active');
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE GroupByExperience()
BEGIN
    SELECT 
        CASE 
            WHEN experience < 1 THEN '0-1'
            WHEN experience < 2 THEN '1-2'
            WHEN experience < 5 THEN '2-5'
            ELSE '5+' 
        END AS experience_range,
        COUNT(*) AS employee_count
    FROM employees
    GROUP BY experience_range;
END$$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE SimulateGlobalIncrement (
    IN increment_percent DECIMAL(5,2)
)
BEGIN
    SELECT 
        name, 
        compensation AS current_compensation,
        ROUND(compensation * (1 + increment_percent / 100), 2) AS updated_compensation
    FROM employees;
END$$

DELIMITER ;
