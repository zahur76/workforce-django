from django.urls import path
from . import views


urlpatterns = [    
    path('', views.staff, name='staff'),
    path('<int:staff_id>', views.staff_details, name='staff_details'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('update_staff/<int:staff_id>', views.update_staff, name='update_staff'),
    path('delete_staff/<int:staff_id>', views.delete_staff, name='delete_staff'),
    path('sick_leave/<int:staff_id>', views.sick_leave, name='sick_leave'),
    path('annual_leave/<int:staff_id>', views.annual_leave, name='annual_leave'),
    path('sick_leave_taken/<int:staff_id>', views.sick_leave_taken, name='sick_leave_taken'),
    path('annual_leave_taken/<int:staff_id>', views.annual_leave_taken, name='annual_leave_taken'),
    path('sick_modify/<int:sick_id>', views.sick_modify, name='sick_modify'),
    path('annual_modify/<int:annual_id>', views.annual_modify, name='annual_modify'),
    path('sick_delete/<int:sick_id>', views.sick_delete, name='sick_delete'),
    path('annual_delete/<int:annual_id>', views.annual_delete, name='annual_delete'),
    path('sick_data', views.sick_data, name='sick_data'),
    path('annual_leave_data', views.annual_leave_data, name='annual_leave_data'),
]