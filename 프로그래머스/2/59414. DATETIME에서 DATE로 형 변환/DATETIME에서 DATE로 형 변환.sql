-- 코드를 입력하세요
SELECT ANIMAL_ID,
       NAME,
       date_format(date(DATETIME),'%Y-%m-%d') '날짜'
from ANIMAL_INS
order by 1