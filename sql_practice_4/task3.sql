CREATE USER hr_user WITH PASSWORD 'admin123';
GRANT SELECT ON Employees TO hr_user;
GRANT INSERT, UPDATE ON Employees TO hr_user;