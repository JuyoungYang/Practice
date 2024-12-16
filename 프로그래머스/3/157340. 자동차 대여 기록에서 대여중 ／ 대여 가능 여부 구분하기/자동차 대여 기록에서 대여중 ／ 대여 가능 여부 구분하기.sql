SELECT CAR_ID,
       CASE 
           WHEN EXISTS (
               SELECT 1
               FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h
               WHERE h.CAR_ID = c.CAR_ID
                 AND h.START_DATE <= '2022-10-16'
                 AND h.END_DATE >= '2022-10-16'
           ) THEN '대여중'
           ELSE '대여 가능'
       END AS AVAILABILITY
FROM (SELECT DISTINCT CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) c
ORDER BY CAR_ID DESC;