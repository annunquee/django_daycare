# Django_daycare/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inbox/', include('inbox.urls')),  # This includes the inbox URLs
    # Other URL patterns...
]
