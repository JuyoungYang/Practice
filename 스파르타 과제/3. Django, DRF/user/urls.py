from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView  # LoginView 추가
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(
        template_name='user/login.html',
        next_page='post:post_list'
    ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='user:login'
    ), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
]