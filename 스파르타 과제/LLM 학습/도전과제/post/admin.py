# post/admin.py
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_filter = ["author", "created_at"]
    search_fields = ["title", "ingredients", "instructions", "author__username"]
