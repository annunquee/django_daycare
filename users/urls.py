from django.urls import path
from .views import projects_list  # Avoid importing the whole views module

urlpatterns = [
    path('', projects_list, name='project_list'),
]
