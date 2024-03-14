-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
