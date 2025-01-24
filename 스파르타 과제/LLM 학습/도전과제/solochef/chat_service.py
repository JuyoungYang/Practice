import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatService:
    @staticmethod
    def today_meal(user_question: str) -> str:
        """메뉴 추천을 요청하고 응답을 반환합니다."""
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

    @staticmethod
    def get_recipe(chosen_menu: str) -> str:
        """선택한 메뉴의 레시피를 가져옵니다."""
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

    @staticmethod
    def get_menu_choice(menu: str, choice: str) -> str:
        """사용자의 메뉴 선택을 처리합니다."""
        menu_lines = menu.split("\n")
        menu_items = []

        for line in menu_lines:
            if line.strip() and line[0].isdigit():
                menu_name = line.split(".")[1].split("-")[0].strip()
                menu_items.append(menu_name)

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(menu_items):
                return menu_items[idx]

        choice = choice.strip().lower()
        for menu in menu_items:
            if choice == menu.lower():
                return menu

        raise ValueError("아 똑바로 하셈!😠")
