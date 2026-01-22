# Write your MySQL query statement below
WITH cte AS (
    SELECT 
    id,
    num,
    LAG(num) OVER(ORDER BY id) AS PREV,
    LEAD(num) OVER(ORDER BY id) AS NEXT
    FROM logs
)
SELECT DISTINCT num 
AS ConsecutiveNums
FROM 
cte 
WHERE num = PREV
AND num = NEXT
