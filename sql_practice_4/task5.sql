CREATE OR REPLACE FUNCTION CalculateAnnualBonus(emp_id INT, salary DECIMAL)
RETURNS DECIMAL AS $$
BEGIN
    RETURN salary * 0.1;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE VIEW IT_Department_View AS
SELECT EmployeeID, FirstName, LastName, Salary
FROM Employees
WHERE Department = 'IT';