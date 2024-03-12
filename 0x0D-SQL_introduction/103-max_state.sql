--Import in hbtn_0c_0 database this table dump by state
SELECT state, MAX(temperature) AS max_temperature FROM weather_data GROUP BY state ORDER BY state;
