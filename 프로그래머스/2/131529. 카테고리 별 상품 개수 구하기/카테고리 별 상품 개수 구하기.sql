-- 코드를 입력하세요
SELECT left(PRODUCT_CODE,2) as CATEGORY,
       count(1) as PRODUCTS
from PRODUCT
group by 1
order by 1