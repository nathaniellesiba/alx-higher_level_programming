-- Import in hbtn_0c_0 database this table dump by month
SELECT city, AVG(value) AS avg_temp
FROM temperatures_by_month
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp
DESC LIMIT 3;
