from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.pay, name="pay"),
    path("add_salary/<int:staff_id>", views.add_salary, name="add_salary"),
    path("salary_details/<int:staff_id>", views.salary_details, name="salary_details"),
    path("salary_delete/<int:salary_id>", views.salary_delete, name="salary_delete"),
    path("salary_update/<int:salary_id>", views.salary_update, name="salary_update"),
    path(
        "employee_salary/<int:salary_id>", views.employee_salary, name="employee_salary"
    ),
]
