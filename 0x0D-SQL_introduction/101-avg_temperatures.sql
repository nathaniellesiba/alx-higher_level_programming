-- Import in hbtn_0c_0 database this table dump
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
