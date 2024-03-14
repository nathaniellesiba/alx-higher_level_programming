-- lists the number of records with the same score
SELECT score, COUNT(*) AS record_count
FROM hbtn_0c_0.second_table
GROUP BY score;
