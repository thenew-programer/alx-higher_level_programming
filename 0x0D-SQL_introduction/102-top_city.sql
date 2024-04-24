-- displays the top 3 of cities temperature during July and August
SELECT TOP 3 city, AVG(value) as avg_temp
    FROM temperatures
    WHERE month LIKE 'July' OR month LIKE 'August'
    GROUP BY city
    ORDER BY avg_temp DESC;
