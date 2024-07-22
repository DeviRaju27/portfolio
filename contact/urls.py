from django.contrib import admin
from django.urls import path
from .views import ContactView, SuccessView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='contact_view'),
    path('success/', SuccessView.as_view(), name='success'),
]