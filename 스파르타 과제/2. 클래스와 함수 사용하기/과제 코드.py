class Person:   #클래스 선언
    def __init__(self, name, gender, age):  #클래스 객체가 생성될 때 자동으로 실행
        self.name = name    
        self.gender = self.validate_gender(gender)  #성별 유효성 검증
        self.age = age

    def validate_gender(self, gender):  #젠더값이 올바른지 확인
        while gender.lower() not in ["m", "f"]: #입력값을 소문자 변환해서 m,f인지 확인
            print("잘못된 성별입니다. 'm' 또는 'f'만 입력하세요.")  #m,f가 아니면 프린트
            gender = input("성별을 다시 입력하세요 (m/f): ")    #m,f가 아니면 재입력 요구
        return "male" if gender.lower() == "m" else "female"    #m은 male, f는 female로 변환

    def display(self):  #메서드
        gender_kor = "남성" if self.gender == "male" else "여성" #셀프젠더값으로 male은 남성, female은 여성으로 변환 출력
        print(f"이름: {self.name}, 성별: {gender_kor}") #에푸스트링을 통해 변수값 문자열 안에 넣고 출력
        print(f"나이: {self.age}")

    def greet(self):    #메서드
        if self.age < 10:
            message = "어린이 여러분! 반가워요!"
        elif self.age < 20:
            message = "청소년 여러분! 반가워요!"
        elif self.age < 30:
            message = "청춘 여러분! 반가워요!"
        elif self.age < 60:
            message = "안녕하세요😘 반갑습니다!"
        else:
            message = "늘 건강하시길🥰 반갑습니다!"
        print(message)      #나이에 따라 다른 인사말을 넣고 프린트


name = input("이름을 입력하세요: ") #사용자 입력 받기
gender = input("성별을 입력하세요 (m/f): ") #사용자 입력 받기

while True: #무한루프 시작
    try:
        age = int(input("나이를 입력하세요: ")) #똑바로 입력하면 무한루프 종료
        break
    except ValueError:     #숫자가 아닌 값을 입력하면 메세지 출력 후 재입력 요구
        print("잘못된 입력입니다. 숫자로 나이를 입력하세요.")

# 클래스 기반으로 이닛 실행
person = Person(name, gender, age)

# 디스플레이를 호출해서 정보 출력
person.display()

# 그릿을 호출해서 나이에 맞는 인사 메시지 출력
person.greet()
