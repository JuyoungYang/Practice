from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/delete/', 
        views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/update/', 
        views.comment_update, name='comment_update'),
]