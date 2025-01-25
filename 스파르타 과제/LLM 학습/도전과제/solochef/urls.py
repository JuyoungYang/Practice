# solochef/urls.py
from django.urls import path
from . import views

app_name = "solochef"

urlpatterns = [
    path("", views.index, name="index"),  # 메인 페이지 (홈)
    path("chat/", views.chat_view, name="chat"),  # 채팅방 페이지
    path("chat/send/", views.chat, name="chat_send"),  # 채팅 처리
    path("recipe/", views.get_recipe, name="recipe"),  # 레시피 처리
]
