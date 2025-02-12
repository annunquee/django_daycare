from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


@login_required
def project_add(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user  # Assign logged-in user
            project.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/project_form.html", {"form": form})

@login_required
def project_edit(request, pk):
    project = Project.objects.get(id=pk)
    if project.user != request.user:  # Prevent editing others' projects
        return redirect("project_list")

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/project_form.html", {"form": form})

@login_required
def project_delete(request, pk):
    project = Project.objects.get(id=pk)
    if project.user == request.user:  # Allow only the owner to delete
        project.delete()
    return redirect("project_list")
