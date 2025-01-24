import datetime
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def today_meal(user_question: str) -> str:
    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": """넌 혼밥 레시피 전문가야. 음슴체로 답해줘. 
                다음 용어들은 모두 음식 추천을 요청하는 표현이야:
                - 오점추: 오늘 점심 추천의 줄임말
                - 오메추: 오늘 메뉴 추천의 줄임말
                - 오저추: 오늘 저녁 추천의 줄임말
                
                사용자 질문에 따라서 음식을 추천해주되,
                만약 위 단어들이 포함되어 있거나 알 수 없는 말이면
                아래 형식으로 랜덤한 3가지 메뉴를 추천해주고 마지막 말도 함께 보여줘.
                
                1. [메뉴명] - [간단한 설명]
                2. [메뉴명] - [간단한 설명]
                3. [메뉴명] - [간단한 설명]
                
                선택지: 1, 2, 3 중에서 골라보셈.""",
            },
            {"role": "user", "content": user_question},
        ],
        model="gpt-4o-mini",
    )

    return response.choices[0].message["content"].strip()


def get_recipe(chosen_menu: str) -> str:
    response = openai.ChatCompletion.create(
        messages=[
            {
                "role": "system",
                "content": """넌 혼밥 레시피 전문가야. 친한 친구처럼 음슴체로 설명해줘.
                다음 형식으로 설명해주고 마지막말 꼭 넣어줘.

                [필요한 재료]
                재료 및 양
                
                [요리순서]
                1. 
                2. 
                ...

                호호 참 쉽죠?🤓""",
            },
            {"role": "user", "content": f"{chosen_menu} 어떻게 만들어?"},
        ],
        model="gpt-4o-mini",
    )

    return response.choices[0].message["content"].strip()


# 텍스트파일 저장
def log_conversation(user_input: str, ai_response: str) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"Timestamp: {current_time}\n")
        file.write(f"User: {user_input}\n")
        file.write(f"AI: {ai_response}\n")
        file.write("=" * 50 + "\n")


def get_menu_choice(menu: str, choice: str) -> str:
    menu_lines = menu.split("\n")
    menu_items = []

    # 추천된 메뉴 목록에서 메뉴 이름만 추출
    for line in menu_lines:
        if line.strip() and line[0].isdigit():
            menu_name = line.split(".")[1].split("-")[0].strip()
            menu_items.append(menu_name)

    # 숫자로 선택한 경우
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(menu_items):
            return menu_items[idx]

    # 메뉴 이름으로 선택한 경우
    choice = choice.strip().lower()
    for menu in menu_items:
        if choice == menu.lower():
            return menu

    raise ValueError("아 똑바로 하셈!😠")


def main():
    print(" ")
    print("하이하이~ 혼밥메뉴 알랴줌! 추천 원하면 말하셈")

    user_question = input("\n오점추? 오메추? 오저추?: ")
    menu = today_meal(user_question)
    print("\n추천 메뉴:")
    print(menu)
    log_conversation(user_question, menu)

    while True:
        choice = input("\n땡기는거 고르셈(1-3): ")
        try:
            chosen_menu = get_menu_choice(menu, choice)
            recipe = get_recipe(chosen_menu)
            print("\n만드는법 알려쥼:")
            print(recipe)
            log_conversation(f"레시피 요청: {chosen_menu}", recipe)
            break

        except ValueError:
            print("아 똑바로 고르셈😠 1-3 숫자나 메뉴 이름 입력하셈!")


if __name__ == "__main__":
    main()
