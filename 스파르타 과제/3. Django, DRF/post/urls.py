from django.urls import path, include
from rest_framework_nested import routers
from . import views

app_name = "post"

router = routers.DefaultRouter()
router.register(r"posts", views.PostViewSet, basename="post")

# 댓글을 위한 중첩 라우터
posts_router = routers.NestedDefaultRouter(router, r"posts", lookup="post")
posts_router.register(r"comments", views.CommentViewSet, basename="post-comments")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
