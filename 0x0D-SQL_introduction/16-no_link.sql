-- lists total records of second table where name is not NULL ordered by score
SELECT score, name
FROM second_table
HAVING name IS NOT NULL
ORDER BY score DESC;
