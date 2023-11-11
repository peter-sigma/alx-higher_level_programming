-- Show the average temperature of city ordered by temperature in descending order

SELECT city, AVG(value)avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
