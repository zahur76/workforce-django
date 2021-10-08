from django.urls import path
from . import views


urlpatterns = [    
    path('', views.staff, name='staff'),
    path('<int:staff_id>', views.staff_details, name='staff_details'),
]