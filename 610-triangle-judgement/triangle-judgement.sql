# Write your MySQL query statement below
WITH cte AS(
    SELECT
    x,y,z,
    x+y AS C1,
    y+z AS C2,
    z+x AS C3
    FROM 
    Triangle
)
SELECT x,y,z,
CASE WHEN C1 > z AND C2 > x AND C3 > y THEN 'Yes' Else 'No' 
END AS triangle
FROM cte;
