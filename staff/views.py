from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import SickLeave, Staff
from .forms import add_staffForm, add_sick_leaveForm
from django.db.models import Q
import datetime


# Create your views here
def staff(request):
    """ A view to return staff info """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home')) 

    elif 'q' in request.GET:
        query = request.GET['q']
        if not query:
            return redirect(reverse('staff'))
        else:                
            all_staff = Staff.objects.all()
            queries = Q(first_name__icontains=query) | Q(last_name__icontains=query)                
            query_staff = all_staff.filter(queries)              
            context = {
                'staff': query_staff,
            }
    else:        
        staff = Staff.objects.all()
        context = {
            'staff': staff,
        }
    
    return render(request, 'staff/staff.html', context)


def staff_details(request, staff_id):
    """ A view to return staff details """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home')) 
    else:
        staff = get_object_or_404(Staff, id=staff_id)        
        context = {
            'staff': staff,
        }
    
    return render(request, 'staff/staff_details.html', context)


def add_staff(request):
    """ A view to add staff details"""
    if request.method == 'POST':
        form = add_staffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Staff Added!')
            return redirect(reverse('staff'))
        else:
            messages.error(
                request, 'Staff could not be added. \
                    Please ensure the form is valid.')
            return redirect(reverse('add_staff'))
    else: 
        form = add_staffForm()

        context = {
            'form': form,        
            }    
    
    return render(request, 'staff/add_staff.html', context)


def update_staff(request, staff_id):
    """ A view to update staff details"""

    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    
    else:
        staff = get_object_or_404(Staff, id=staff_id)          
        if request.method == 'POST':        
            form = add_staffForm(request.POST, request.FILES, instance=staff)
            if form.is_valid():
                form.save()
                messages.success(request, 'Staff updated!')
                return redirect(reverse('staff_details', args=[staff_id]))
            else:
                messages.error(
                    request, 'Staff could not be added. \
                        Please ensure the form is valid.')
                return redirect(reverse('update_staff', args={staff_id}))
        else:                    
            form = add_staffForm(instance=staff)

            context = {
                'form': form,
                'staff': staff,
                }

    return render(request, 'staff/update_staff.html', context)


def delete_staff(request, staff_id):
    """ A view to update staff details"""

    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        staff = get_object_or_404(Staff, id=staff_id)
        staff.delete()
        messages.success(request, 'Staff record deleted!')
        return redirect(reverse('staff'))


def sick_leave(request, staff_id):
    """ A view to input sick leave details"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))    
    else:        
        staff = get_object_or_404(Staff, id=staff_id)
        leave_periods =  SickLeave.objects.all().filter(staff__id=staff_id)                 
        if request.method == 'POST':                    
            form = add_sick_leaveForm(request.POST)            
            if form.is_valid():                                
                sick = form.save(commit=False)
                if leave_periods:
                    count =0
                    day_list = []
                    for leave in leave_periods:
                        sick_days = (leave.end_date-leave.start_date).days + 1                        
                        for x in range(0, sick_days):
                            day_list.append(leave.start_date + datetime.timedelta(days = x))                                                       
                    for x in range (0,(sick.end_date-sick.start_date).days+1):                        
                        if (sick.start_date + datetime.timedelta(days = x)) in day_list:                            
                            count += 1                           
                        else:
                            count += 0                                          
                    if count !=0:
                        messages.error(request, 'Error Duplicate dates!')
                        return redirect(reverse('staff_details', args=[staff_id]))
                    else:
                        if sick.end_date<sick.start_date:
                            messages.error(request, 'Dates incorrect!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                        else:
                            difference = (sick.end_date - sick.start_date).days + 1                                       
                            staff.sick_leave_remaining = staff.sick_leave_remaining - difference 
                            staff.save()                                     
                            sick.staff = staff
                            sick.days = difference
                            sick.save()                    
                            messages.success(request, 'Sick leave added!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                else:
                    if sick.end_date<sick.start_date:
                            messages.error(request, 'Dates incorrect!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                    else:
                        difference = (sick.end_date - sick.start_date).days + 1                                       
                        staff.sick_leave_remaining = staff.sick_leave_remaining - difference 
                        staff.save()                                     
                        sick.staff = staff
                        sick.days = difference
                        sick.save()                    
                        messages.success(request, 'Sick leave added!')
                        return redirect(reverse('staff_details', args=[staff_id]))

            else:                
                messages.error(
                    request, 'Sick leave could not be added. \
                        Please ensure the form is invalid.')
                return redirect(reverse('staff_details', args={staff_id}))
        else:          
            form = add_sick_leaveForm(instance=staff)

            context = {
                'form': form,
                'staff': staff,
            }

    return render(request, 'staff/sick_leave.html', context)


def sick_leave_taken(request, staff_id):
    """ A view for sick leave taken"""

    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        staff = get_object_or_404(Staff, id=staff_id)
        sick_leave = SickLeave.objects.all()
        sick_leave = sick_leave.filter(staff__id=staff_id)
        context = {
            'staff': staff,
            'sick_leave': sick_leave,
        }        
        return render(request, 'staff/sick_leave_taken.html', context)



def sick_modify(request, sick_id):
    """ A view for sick leave taken"""

    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        sick = get_object_or_404(SickLeave, id=sick_id)        
        staff = get_object_or_404(Staff, first_name=sick.staff.first_name)        
        original_difference = (sick.end_date - sick.start_date).days + 1
        leave_periods =  SickLeave.objects.all().filter(staff__id=staff.id).exclude(id=sick_id)              
        if request.method == 'POST':
            form = add_sick_leaveForm(request.POST, instance=sick)
            if form.is_valid():
                modified_sick = form.save(commit=False)
                if leave_periods:
                    count =0
                    day_list = []
                    for leave in leave_periods:
                        sick_days = (leave.end_date-leave.start_date).days + 1                        
                        for x in range(0, sick_days):
                            day_list.append(leave.start_date + datetime.timedelta(days = x))                                                       
                    for x in range (0,(modified_sick.end_date-modified_sick.start_date).days+1):                        
                        if (sick.start_date + datetime.timedelta(days = x)) in day_list:                            
                            count += 1                           
                        else:
                            count += 0                                          
                    if count !=0:
                        messages.error(request, 'Error Duplicate dates!')
                        return redirect(reverse('sick_leave_taken', args=[sick.staff_id]))
                    else:                        
                        if modified_sick.end_date<modified_sick.start_date:
                            messages.error(request, 'Dates incorrect!')
                            return redirect(reverse('sick_leave_taken', args=[sick.staff_id]))
                        else:
                            modified_difference = (modified_sick.end_date - modified_sick.start_date).days + 1                 
                            staff.sick_leave_remaining = staff.sick_leave_remaining + original_difference - modified_difference 
                            staff.save()
                            modified_sick.days = modified_difference                    
                            modified_sick.save()
                            return redirect(reverse('sick_leave_taken', args={sick.staff.id}))
                else:
                    if modified_sick.end_date<modified_sick.start_date:
                            messages.error(request, 'Dates incorrect!')
                            return redirect(reverse('sick_leave_taken', args=[sick.staff_id]))
                    else:
                        modified_difference = (modified_sick.end_date - modified_sick.start_date).days + 1                 
                        staff.sick_leave_remaining = staff.sick_leave_remaining + original_difference - modified_difference 
                        staff.save()
                        modified_sick.days = modified_difference                    
                        modified_sick.save()
                        return redirect(reverse('sick_leave_taken', args={sick.staff.id}))

            else:
                messages.error(
                    request, 'Sick leave could not be modified. \
                        Please ensure the form is invalid.')
                return redirect(reverse('sick_leave_taken', args={sick.staff.id}))

        else:          
            
            form = add_sick_leaveForm(instance=sick) 
            context = {
                'sick':sick,
                'form': form,            
            }        
        return render(request, 'staff/sick_modify.html', context)


def sick_delete(request, sick_id):
    """ A view to delete sick leave"""

    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        sick = get_object_or_404(SickLeave, id=sick_id)
        staff = get_object_or_404(Staff, first_name=sick.staff.first_name)       
        staff.sick_leave_remaining = staff.sick_leave_remaining + sick.days
        staff.save()
        sick.delete()
        return redirect(reverse('sick_leave_taken', args={sick.staff.id}))