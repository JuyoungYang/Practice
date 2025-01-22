# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ("id", "username", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active", "date_joined")
    fieldsets = UserAdmin.fieldsets + (
        ("추가 정보", {"fields": ("profile_image", "bio")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "추가 정보",
            {
                "fields": ("email", "profile_image", "bio"),
            },
        ),
    )
    search_fields = ("username", "email", "bio")
    ordering = ("-date_joined",)
