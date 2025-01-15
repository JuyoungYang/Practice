from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserUpdateForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/signup.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/profile.html', {'user': request.user})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'user/profile_update.html', {'form': form})