from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects_list = Project.objects.all()
    context = {
        'projects': projects_list
    }
    return render(request, 'blog/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    context = {
        'project': project_obj
    }
    return render(request, 'blog/project.html', context)


def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'blog/create_project.html', {'form': form})


def update_project(request, pk):
    project_obj = Project.objects.get(id=pk)
    form = ProjectForm(instance=project_obj)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_obj)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'blog/create_project.html', {'form': form})


def delete_project(request, pk):
    project_obj = Project.objects.get(id=pk)

    if request.method == 'POST':
        project_obj.delete()
        return redirect('projects')

    return render(request, 'blog/delete.html', {'obj': project_obj})
