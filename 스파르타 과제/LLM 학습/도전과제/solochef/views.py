from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChatForm
from .models import Conversation
from .chat_service import ChatService
from django.http import JsonResponse


def index(request):
    """메인 페이지"""
    return render(request, "solochef/index.html")


def chat_view(request):
    """채팅 페이지"""
    chat_form = ChatForm()
    conversations = Conversation.objects.order_by("timestamp")[:5]
    return render(
        request,
        "solochef/chat.html",
        {"chat_form": chat_form, "conversations": conversations},
    )


def chat(request):
    """채팅 메시지 처리"""
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data["message"]
            chat_service = ChatService()

            try:
                response = chat_service.today_meal(user_input)
                conversation = Conversation.objects.create(
                    user_input=user_input, ai_response=response
                )
                return JsonResponse(
                    {
                        "status": "success",
                        "response": response,
                        "conversation_id": conversation.id,
                    }
                )
            except Exception as e:
                return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "잘못된 요청입니다."})


def get_recipe(request):
    """레시피 처리"""
    if request.method == "POST":
        choice = request.POST.get("choice")
        menu = request.POST.get("menu", "")
        chat_service = ChatService()

        try:
            chosen_menu = chat_service.get_menu_choice(menu, choice)
            recipe = chat_service.get_recipe(chosen_menu)
            conversation = Conversation.objects.create(
                user_input=f"레시피 요청: {chosen_menu}", ai_response=recipe
            )
            return JsonResponse(
                {
                    "status": "success",
                    "recipe": recipe,
                    "conversation_id": conversation.id,
                }
            )
        except ValueError as e:
            return JsonResponse({"status": "error", "message": str(e)})
    return JsonResponse({"status": "error", "message": "잘못된 요청입니다."})
