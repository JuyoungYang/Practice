from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = "accounts"

urlpatterns = [
    # 회원가입
    path("signup/", views.SignupView.as_view(), name="signup"),
    # 토큰 기반 로그인
    path("login/", obtain_auth_token, name="login"),
    # 프로필 보기/수정
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("profile/update/", views.ProfileUpdateView.as_view(), name="profile_update"),
]
