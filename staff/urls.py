from django.urls import path
from . import views


urlpatterns = [    
    path('', views.staff, name='staff'),
    path('<int:staff_id>', views.staff_details, name='staff_details'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('update_staff/<int:staff_id>', views.update_staff, name='update_staff'),
]