from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.pay, name='pay'),
    path('add_salary/<int:integer>', views.add_salary, name='add_salary'),
]
