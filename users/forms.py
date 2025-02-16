from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "address", "password1", "password2")

class UserUpdateForm(forms.ModelForm):
    # Overriding the default __init__ to add some styling options (optional)
    class Meta:
        model = CustomUser  # Use CustomUser here, not the default User model
        fields = ['username', 'email', 'phone', 'address']

    # Optional: Add validation or other customization here if needed

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
