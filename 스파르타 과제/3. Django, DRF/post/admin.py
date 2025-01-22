# posts/admin.py
from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "created_at",
        "status",
        "view_count",
        "total_likes",
    )
    list_filter = ("status", "created_at")
    search_fields = ("title", "content", "author__username")
    readonly_fields = ("id", "created_at", "updated_at", "view_count")

    def total_likes(self, obj):
        return obj.likes.count()

    total_likes.short_description = "좋아요 수"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "__str__", "author", "post", "created_at", "is_active")
    list_filter = ("is_active", "created_at")
    search_fields = ("content", "author__username", "post__title")
    readonly_fields = ("created_at", "updated_at")
