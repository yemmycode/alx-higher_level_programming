-- This displays the average temperature by city in a descending order
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
