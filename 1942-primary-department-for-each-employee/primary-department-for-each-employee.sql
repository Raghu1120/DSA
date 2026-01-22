# Write your MySQL query statement below
WITH count_cte AS (
    SELECT
    employee_id,
    department_id,
    primary_flag,
    COUNT(*) OVER (PARTITION BY employee_id) AS CNT
    FROM Employee
)
SELECT employee_id,department_id
FROM count_cte
WHERE primary_flag = 'Y'
OR CNT = 1