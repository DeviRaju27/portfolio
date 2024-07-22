from django.shortcuts import render
from .models import Projects

def projects_index(request):
    projects = Projects.objects.all()

    context = { 'projects' : projects }

    return render(request, 'projects/projects_index.html', context)

def projects_detail(request, pk):
    project = Projects.objects.get(pk=pk)

    context = { 'project' : project }

    return render(request, 'projects/projects_details.html', context)