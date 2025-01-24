from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ChatForm
from .models import Conversation
from .chat_service import ChatService


def index(request):
    chat_form = ChatForm()
    # 이전 대화 내역을 가져옵니다
    conversations = Conversation.objects.all().order_by("timestamp")[:5]
    return render(
        request,
        "solochef/index.html",
        {
            "chat_form": chat_form,
            "conversations": conversations,
            "menu_response": None,  # 초기에는 메뉴 응답이 없습니다
        },
    )


def chat(request):
    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data["message"]
            chat_service = ChatService()

            try:
                response = chat_service.today_meal(user_input)
                # 대화 내용을 저장합니다
                conversation = Conversation.objects.create(
                    user_input=user_input, ai_response=response
                )
                # POST-Redirect-GET 패턴을 사용하여 결과 페이지로 이동합니다
                return render(
                    request,
                    "solochef/index.html",
                    {
                        "chat_form": ChatForm(),
                        "menu_response": response,
                        "conversations": Conversation.objects.all().order_by(
                            "-timestamp"
                        )[:5],
                    },
                )
            except Exception as e:
                messages.error(request, str(e))

    return redirect("solochef:index")


def get_recipe(request):
    if request.method == "POST":
        choice = request.POST.get("choice")
        menu = request.POST.get("menu", "")
        chat_service = ChatService()

        try:
            chosen_menu = chat_service.get_menu_choice(menu, choice)
            recipe = chat_service.get_recipe(chosen_menu)
            # 레시피 요청 내용을 저장합니다
            conversation = Conversation.objects.create(
                user_input=f"레시피 요청: {chosen_menu}", ai_response=recipe
            )
            return render(
                request,
                "solochef/index.html",
                {
                    "chat_form": ChatForm(),
                    "recipe_response": recipe,
                    "conversations": Conversation.objects.all().order_by("-timestamp")[
                        :5
                    ],
                },
            )
        except ValueError as e:
            messages.error(request, str(e))

    return redirect("solochef:index")
