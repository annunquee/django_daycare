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

     # Password Reset URLs (built-in auth views)
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'
    ),
]
