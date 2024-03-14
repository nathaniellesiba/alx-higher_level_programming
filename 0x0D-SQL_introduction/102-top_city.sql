-- Import in hbtn_0c_0 database this table dump by month
SELECT city, MAX(value) AS max_temperature FROM weather_data WHERE MONTH(date) IN (7, 8) GROUP BY city ORDER BY max_temperature DESC LIMIT 3;
