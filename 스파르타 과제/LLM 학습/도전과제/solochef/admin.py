from django.contrib import admin
from .models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):

    list_display = ["timestamp", "user_input", "ai_response"]
    list_filter = ["timestamp"]
    search_fields = ["user_input", "ai_response"]
