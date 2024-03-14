-- Import in hbtn_0c_0 database this table dump
SELECT city, AVG(temperature) as average_temperature_fahrenheit
FROM weather_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
