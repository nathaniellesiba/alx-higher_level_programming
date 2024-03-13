-- creates a table second_table in the db hbtn_0c_0
CREATE TABLE second_table (
    id INT,
    name VARCHAR(50),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
SELECT id, name, score
FROM second_table;
