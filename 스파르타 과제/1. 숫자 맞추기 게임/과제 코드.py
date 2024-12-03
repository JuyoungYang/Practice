import random     #랜덤 모듈 불러오기 
def start_game(): #게임 시작 함수   

    while True:                                 #게임을 그만둘 때까지 무한 반복 시작
        chosen_number = random.randint(1, 10)   #1과 10 사이의 랜덤한 숫자 선택   
        print("=== 숫자 맞추기 게임 ===")           #게임 시작 문구 출력
        print(f"1과 10 사이의 숫자를 하나 정했습니다.\n이 숫자는 무엇일까요?") #게임 설명 출력

        while True:                                         #정답이 나올 때까지 무한 반복 시작
            try:                                            #예외 처리 시작
                user_number = int(input("예상 숫자 : "))      #사용자 입력 숫자로 받기
                if not (1 <= user_number <= 10):            #사용자 입력 숫자가 1과 10 사이가 아니면
                    print("입력값이 1과 10 사이가 아닙니다. 다시 입력하세요.") #해당 메세지 출력   
                    continue                                 #1과 10 사이가 아니면 다시 입력하기
                if user_number < chosen_number:              #사용자 입력 숫자가 정답보다 작으면   
                    print("너무 작습니다. 다시 입력하세요.")        #해당 메세지 출력
                elif user_number > chosen_number:            #사용자 입력 숫자가 정답보다 크면
                    print("너무 큽니다. 다시 입력하세요.")          #해당 메세지 출력
                elif user_number == chosen_number:           #사용자 입력 숫자가 정답과 같으면
                    print("정답입니다!")                        #해당 메세지 출력
                    break                                    #정답이 나오면 반복문 종료
            except ValueError:                               #밸류에러일 때
                print("유효하지 않은 숫자입니다. 숫자를 입력해주세요.") #해당 메세지 출력   
        
        while True:                                            #게임을 계속 할지 말지 묻는 반복문 시작
            user_input = input("계속 하시겠습니까? (Y/N): ").strip().upper() #사용자에게 받은 입력을 공백 제거 후 대문자로 변환
            if user_input == 'Y':                              #사용자 입력이 Y이면
                break                                          #반복문 종료
            elif user_input == 'N':                            #사용자 입력이 N이면
                print("게임을 종료합니다.")                        #해당 메세지 출력 후
                return                                         #게임 종료
            else:                                              #사용자 입력이 Y와 N이 아니면
                print("잘못된 입력입니다. Y 또는 N을 입력하세요.")      #해당 메세지 출력

start_game()                                                   #Y를 선택하면 루프 탈출 후 시작함수 호출
