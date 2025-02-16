from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import UserUpdateForm, ProfileUpdateForm, CustomUserCreationForm
from .models import Profile

# Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("project_list")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

# Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("project_list")
    return render(request, "users/login.html")

# Logout View
def user_logout(request):
    logout(request)
    return redirect("project_list")

# Profile Update View
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

# Test Template View (for debugging template loading)
def test_template(request):
    try:
        template = get_template("users/password_reset.html")
        return HttpResponse(f"Template found: {template.name}")
    except Exception as e:
        return HttpResponse(f"Error loading template: {e}")
