from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
from django.utils import timezone

from .models import Project
from .forms import ProjectForm

# Create your views here.

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ProjectForm()
            messages.success(request, ("New project has been created"))
            return redirect('add-project') 
        else:
            messages.error(request, ("There was an error with your project."))
            return render(request, 'projects/add_project.html', {})
    form = ProjectForm
    return render(request, 'projects/add_project.html', {'form': form})

def all_projects(request):
    projects = Project.objects.all().order_by('-time_created')
    context = {
        'projects' : projects
    }
    return render(request, 'projects/projects.html', context)


def update_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = ProjectForm
            messages.success(request, ("The project has been updated."))
            return redirect('all-projects')
        else:
            messages.error(request, ("There was an error with your form. Try again"))
            return render(request, 'projects/update_project.html', {})
    
    return render(request, 'projects/update_project.html', {'form': form, 'project': project })



def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, ("The {} project has been deleted.".format(project.name)))
        return redirect('all-projects')  
    return render(request, 'projects/projects.html', {})  


def click_delete(request, project_id):
    click_delete = True
    all_projects = Project.objects.all()
    project = Project.objects.get(pk=project_id) 
    return render(request, 'projects/projects.html', {'all_projects': all_projects, 'click_delete': click_delete, 'project': project})

def search_projects(request):
    search = None
    if request.method == "POST":
        q = request.POST['q']
        if q:
            search = Project.objects.distinct().filter(
                Q(name__icontains=q) |
                Q(description__icontains=q)

            )

    return render(request, 'projects/search_projects.html', {'q': q, 'search': search})

