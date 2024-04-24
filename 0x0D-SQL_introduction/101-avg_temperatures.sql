-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
USE hbtn_0c_c;
source ./temperatures.sql;
SELECT city, AVG(value) as avg_temp
    FROM temperature
    GROUP BY city
    ORDER BY avg_temp DESC;
