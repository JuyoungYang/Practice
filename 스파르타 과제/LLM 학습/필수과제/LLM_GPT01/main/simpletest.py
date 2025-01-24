import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a tour guide in Korea.",
        },  # 프롬프트 명령
        {"role": "user", "content": "제주도는 어떤곳이야?"},  # 사용자 입력
    ],
)

print(response["choices"][0]["message"]["content"])
