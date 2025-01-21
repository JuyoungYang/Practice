from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "post"

router = DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")

# 댓글을 위한 중첩 라우터
post_comment_router = DefaultRouter()
post_comment_router.register(r"comments", views.CommentViewSet, basename="comment")

urlpatterns = [
    path("", include(router.urls)),
    # 중첩된 댓글 URL - posts/<post_pk>/comments/
    path("posts/<int:post_pk>/", include(post_comment_router.urls)),
]
