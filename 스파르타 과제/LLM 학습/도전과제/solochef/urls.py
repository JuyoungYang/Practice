from django.urls import path
from . import views

app_name = "solochef"

urlpatterns = [
    path("", views.index, name="index"),  # 메인 페이지
    path("chat/", views.chat, name="chat"),  # 채팅 처리
    path("recipe/", views.get_recipe, name="recipe"),  # 레시피 처리
]
