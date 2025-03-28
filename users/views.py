from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import UserUpdateForm, ProfileUpdateForm, CustomUserCreationForm
from .models import Profile

# ✅ Secure: Only staff members can reset the admin password
@staff_member_required
def set_admin_password(request):
    User = get_user_model()
    admin = User.objects.filter(username="admin").first()
    if admin:
        admin.set_password("YourNewSecurePassword")
        admin.save()
        return HttpResponse("Admin password updated successfully.")
    return HttpResponse("Admin user not found.")

# ✅ Register View
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy("project_list"))  # Redirect using reverse_lazy
    else:
        form = CustomUserCreationForm()  # Fixed incorrect form initialization
    return render(request, "users/register.html", {"form": form})

# ✅ Login View with Error Handling
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse_lazy("project_list"))
        else:
            messages.error(request, "Invalid username or password!")  # Show error message
    return render(request, "users/login.html")

# ✅ Logout View
def user_logout(request):
    logout(request)
    return redirect(reverse_lazy("project_list"))

# ✅ Profile Update View
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect(reverse_lazy("profile"))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "users/profile.html", context)

# ✅ Test Template View (for debugging)
def test_template(request):
    try:
        template = get_template("users/password_reset.html")
        return HttpResponse(f"Template found: {template.name}")
    except Exception as e:
        return HttpResponse(f"Error loading template: {e}")
