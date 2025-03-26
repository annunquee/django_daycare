from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # User Registration
    path('register/', views.register, name="register"),

    # User Login
    path('login/', views.user_login, name="login"),

    # User Logout
    path("logout/", views.user_logout, name="logout"),

    # Test Template Loading (for debugging purposes)
    path("test-template/", views.test_template, name="test_template"),

]
