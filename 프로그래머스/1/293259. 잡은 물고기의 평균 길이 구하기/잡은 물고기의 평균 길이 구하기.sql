select ROUND(AVG(CASE 
                    WHEN length is null THEN 10
                    ELSE length END), 2) AS AVERAGE_LENGTH
from FISH_INFO