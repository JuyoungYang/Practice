# post/urls.py
from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.post_list, name="list"),
    path("write/", views.post_write, name="write"),
    path("<int:pk>/", views.post_detail, name="detail"),
]
