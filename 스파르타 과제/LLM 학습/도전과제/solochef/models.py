from django.db import models
from django.utils import timezone
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class Conversation(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    user_input = models.TextField(verbose_name="사용자 입력")
    ai_response = models.TextField(verbose_name="AI 응답")

    class Meta:
        ordering = ["-timestamp"]
        verbose_name = "대화"
        verbose_name_plural = "대화 기록"

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M')} 대화"
