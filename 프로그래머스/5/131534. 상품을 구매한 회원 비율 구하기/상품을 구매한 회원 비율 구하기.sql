SELECT DATE_FORMAT(O.SALES_DATE, '%Y') AS YEAR,
        DATE_FORMAT(O.SALES_DATE, '%m') AS MONTH,
        COUNT(DISTINCT U.USER_ID) AS PUCHASED_USERS,
        ROUND(COUNT(DISTINCT U.USER_ID)/(SELECT COUNT(*) FROM USER_INFO WHERE joined LIKE '2021%'), 1) AS PUCHASED_RATIO
FROM USER_INFO U
JOIN ONLINE_SALE O
ON U.USER_ID = O.USER_ID
#join 된 테이블 결과는 한 회원이 여러 번 구매 이력이 있을 수 있기 때문에 distinct를 이용하여 중복 회원 id를 제거해 준 뒤 count를 세줘야 한다.
WHERE U.JOINED LIKE '2021%'
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH
;