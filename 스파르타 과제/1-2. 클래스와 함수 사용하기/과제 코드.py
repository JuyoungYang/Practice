def good_gender():  #메서드     
    while True:     #무한루프    
        gender = input("성별을 입력하세요 (m/f): ").lower()  #사용자 입력값을 소문자로 변환
        if gender in ["m", "f"]:                         #사용자 입력값이 m,f면
            return "male" if gender == "m" else "female" #m은 male, f는 female로 변환 출력  
        print("잘못된 성별입니다. 'm' 또는 'f'만 입력하세요.")    #사용자 입력값이 m,f가 아니면 프린트


def good_age():  #메서드
    while True:  #무한루프
        try:     #예외처리
            age = int(input("나이를 입력하세요: "))        #사용자 입력값을 정수로 변환
            if age > 0:                                #나이가 양수면
                return age                             #나이 출력
            else:                                      #나이가 양수가 아니면
                print("나이는 양수여야 합니다.")             #해당 메세지 프린트
        except ValueError:                             #밸류에러가 나면
            print("잘못된 입력입니다. 숫자로 나이를 입력하세요.") #해당 메세지 프린트


class Person:  #클래스
    def __init__(self, name, gender, age):    #클래스 객체가 생성될 때 자동으로 실행
        self.name = name                      #셀프네임값에 사용자 입력값 넣기
        self.gender = gender                  #셀프젠더값에 사용자 입력값 넣기
        self.age = age                        #셀프나이값에 사용자 입력값 넣기

    def display(self):  #메서드
        gender_kor = "남성" if self.gender == "male" else "여성" #셀프젠더값으로 male은 남성, female은 여성으로 변환 출력   
        print(f"이름: {self.name}, 성별: {gender_kor}")          #에푸스트링을 통해 변수값 문자열 안에 넣고 출력 
        print(f"나이: {self.age}")                              #에푸스트링을 통해 변수값 문자열 안에 넣고 출력

    def greet(self):  #메서드, 각 조건에 맞는 메세지 출력
        if self.age < 10:
            message = "어린이 여러분! 반가워요!"
        elif self.age < 20:
            message = "청소년 여러분! 반가워요!"
        elif self.age < 40:
            message = "청춘 여러분! 반가워요!"
        elif self.age < 60:
            message = "안녕하세요😘 반갑습니다!"
        else:
            message = "늘 건강하시길🥰 반갑습니다!"
        print(message) 


# 사용자 입력
name = input("이름을 입력하세요: ")
gender = good_gender()  # 성별 검증
age = good_age()        # 나이 검증

# Person 객체 생성 및 출력
person = Person(name, gender, age)
person.display()
person.greet()
