yeondo = int(input())
#윤년 : 4의 배수이고 100의 배수 아니고, 400의 배수
if yeondo%4==0 and yeondo%100!=0 :
    print("1")
elif yeondo%400==0 :
    print("1") 
else : 
    print("0")