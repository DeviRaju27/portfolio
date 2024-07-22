from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_index, name='projects_index'),
    path('<int:pk>/', views.projects_detail, name='projects_detail'),
]