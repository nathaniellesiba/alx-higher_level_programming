-- Import in hbtn_0c_0 database this table dump
SELECT city, AVG(temperature) AS avg_temp
FROM weather_data
GROUP BY city;
