-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
	    id INT NOT NULL AUTO_INCREMENT,
	    name VARCHAR(255) NOT NULL,
	    PRIMARY KEY (id)
	);
