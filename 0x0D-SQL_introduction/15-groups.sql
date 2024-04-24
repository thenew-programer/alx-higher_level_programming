-- lists the number of records with the same score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
HAVING  > 1;
ORDER BY number DESC
