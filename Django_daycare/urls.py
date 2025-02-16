"""
URL configuration for Django_daycare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import views as auth_views

# Simple view for homepage
def home(request):
    return HttpResponse("Welcome to the homepage!")

urlpatterns = [
    # Homepage
    path('', home, name='home'),

    # Admin URL
    path('admin/', admin.site.urls),

    # Include other app URLs
    path('projects/', include('projects.urls')),
    path('users/', include('users.urls')),
    path('inbox/', include('inbox.urls')),

   
]

# Serve static files during development (when DEBUG is True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
