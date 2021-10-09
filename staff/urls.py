from django.urls import path
from . import views


urlpatterns = [    
    path('', views.staff, name='staff'),
    path('<int:staff_id>', views.staff_details, name='staff_details'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('update_staff/<int:staff_id>', views.update_staff, name='update_staff'),
    path('delete_staff/<int:staff_id>', views.delete_staff, name='delete_staff'),
    path('sick_leave/<int:staff_id>', views.sick_leave, name='sick_leave'),
]