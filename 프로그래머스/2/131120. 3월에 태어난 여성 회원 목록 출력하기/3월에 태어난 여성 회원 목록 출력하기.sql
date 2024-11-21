-- 코드를 입력하세요
SELECT MEMBER_ID,
       MEMBER_NAME,
       GENDER, 
       date_format(date(DATE_OF_BIRTH), '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W' 
      and DATE_OF_BIRTH like '%03%'
      and TLNO is not null
order by 1