UPDATE Employees
SET Salary = Salary * 1.1
WHERE Department = 'HR';
UPDATE Employees
SET Department = 'Senior IT'
WHERE Salary > 70000;
DELETE FROM Employees
WHERE NOT EXISTS (
    SELECT * FROM EmployeeProjects
    WHERE EmployeeProjects.EmployeeID = Employees.EmployeeID
);
BEGIN;

INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
VALUES ('New Project', 50000.00, '2026-08-24', '2027-08-24');

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
VALUES 
((SELECT EmployeeID FROM Employees WHERE FirstName = 'Alice' AND LastName = 'Smith'), 
 (SELECT ProjectID FROM Projects WHERE ProjectName = 'New Project'), 100),
((SELECT EmployeeID FROM Employees WHERE FirstName = 'Bob' AND LastName = 'Johnson'), 
 (SELECT ProjectID FROM Projects WHERE ProjectName = 'New Project'), 120);

COMMIT;