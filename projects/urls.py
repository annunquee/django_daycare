from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),  # Should work now
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("add/", views.project_add, name="project_add"),
    path("<int:pk>/edit/", views.project_edit, name="project_edit"),
    path("<int:pk>/delete/", views.project_delete, name="project_delete"),
]
