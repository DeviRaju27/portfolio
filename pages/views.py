from django.shortcuts import render
from projects.models import Projects

def home(request):
    projects = Projects.objects.all()
    return render(request, 'pages/home.html', {'projects': projects})

def about(request):
    return render(request, 'pages/about.html', {})