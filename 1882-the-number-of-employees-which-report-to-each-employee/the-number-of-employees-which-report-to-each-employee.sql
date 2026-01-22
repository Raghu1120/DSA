# Write your MySQL query statement below
WITH CTE AS (
    SELECT 
    employee_id,
    name,
    reports_to,
    age 
    FROM Employees
    WHERE reports_to IS NOT NULL
)
SELECT e.employee_id,
e.name,
COUNT(c.employee_id) AS reports_count,
ROUND(AVG(c.age)) AS average_age
FROM Employees e
JOIN CTE c
ON 
e.employee_id = c.reports_to
GROUP BY e.employee_id ,e.name
ORDER BY e.employee_id 