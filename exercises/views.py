from django.shortcuts import render
from .models import Exercises
# Create your views here.
def exercises_index(request):
    exercises = Exercises.objects.all()

    context = { 'exercises' : exercises }

    return render(request, 'exercises/exercises_index.html', context)

def exercises_details(request, pk):
    exercise = Exercises.objects.get(pk=pk)

    context = { 'exercise' : exercise }

    return render(request, 'exercises/exercises_details.html', context)