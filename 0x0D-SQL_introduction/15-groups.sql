--  script that lists the number of records with the same score in the table
SELECT count(*) AS number, score FROM second_table GROUP BY score;
