-- 코드를 입력하세요
SELECT ANIMAL_ID,
       name
from ANIMAL_INS
where name like '%el%'
      and ANIMAL_TYPE = 'dog'
order by name