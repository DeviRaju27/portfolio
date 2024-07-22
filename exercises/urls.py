from django.urls import path
from exercises import views

app_name = 'exercises'

urlpatterns = [
    path('', views.exercises_index, name='exercises_index'),
    path('<int:pk>/', views.exercises_details, name='exercises_details'),
]