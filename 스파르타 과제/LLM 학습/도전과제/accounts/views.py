# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignupForm, LoginForm, UserUpdateForm, CustomPasswordChangeForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("solochef:index")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("solochef:index")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    return redirect("solochef:index")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


@login_required
def update(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "회원정보가 수정되었습니다.")
            return redirect("accounts:profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "accounts/update.html", {"form": form})


@login_required
def password_change(request):
    if request.method == "POST":
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호가 변경되었습니다.")
            return redirect("accounts:profile")
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, "accounts/password_change.html", {"form": form})


@login_required
def delete(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        messages.success(request, "회원탈퇴가 완료되었습니다.")
        return redirect("solochef:index")
    return render(request, "accounts/delete.html")
