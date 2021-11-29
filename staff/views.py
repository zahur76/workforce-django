from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import AnnualLeave, SickLeave, Staff
from .forms import add_staffForm, add_sick_leaveForm, add_annual_leaveForm
from django.db.models import Q
import datetime
import json
from calendar import monthrange


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
            return render(request, 'staff/staff.html', context)
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
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))

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
        sick_leave_periods =  SickLeave.objects.all().filter(staff__id=staff_id)
        annual_leave_periods =  AnnualLeave.objects.all().filter(staff__id=staff_id)                      
        if request.method == 'POST':                    
            form = add_sick_leaveForm(request.POST)                      
            if form.is_valid():                                               
                sick = form.save(commit=False)                
                actual_year = datetime.datetime.now().strftime("%y")
                sick_start_year = sick.start_date.strftime("%y")
                sick_end_year = sick.end_date.strftime("%y")
                if sick_start_year != sick_end_year:
                    messages.error(request, f'Entry allowed for 1 year only!, e.g 20{actual_year}')
                    return redirect(reverse('staff_details', args=[staff_id]))
                elif sick.end_date<sick.start_date:
                    messages.error(request, 'Start date Incorrect')
                    return redirect(reverse('staff_details', args=[staff_id]))
                elif actual_year != sick_start_year and actual_year != sick_end_year:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            sick_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, sick_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x)) 
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
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
                            difference = (sick.end_date - sick.start_date).days + 1
                            sick.staff = staff
                            sick.days = difference
                            sick.save()
                            messages.success(request, 'Sick leave added!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                    else:
                        difference = (sick.end_date - sick.start_date).days + 1            
                        staff.save()                                     
                        sick.staff = staff
                        sick.days = difference
                        sick.save()                    
                        messages.success(request, 'Sick leave added!')
                        return redirect(reverse('staff_details', args=[staff_id]))
                else:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            sick_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, sick_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x)) 
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
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
                            difference = (sick.end_date - sick.start_date).days + 1                                       
                            staff.sick_leave_remaining = staff.sick_leave_remaining - difference 
                            staff.save()                                     
                            sick.staff = staff
                            sick.days = difference
                            sick.save()                    
                            messages.success(request, 'Sick leave added!')
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


def annual_leave(request, staff_id):
    """ A view to input annual leave details"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        staff = get_object_or_404(Staff, id=staff_id)
        sick_leave_periods =  SickLeave.objects.all().filter(staff__id=staff_id)
        annual_leave_periods =  AnnualLeave.objects.all().filter(staff__id=staff_id)
        if request.method == 'POST':
            form = add_annual_leaveForm(request.POST)
            if form.is_valid():
                annual = form.save(commit=False)
                actual_year = datetime.datetime.now().strftime("%y")
                annual_start_year = annual.start_date.strftime("%y")
                annual_end_year = annual.end_date.strftime("%y")
                if annual_start_year != annual_end_year:
                    messages.error(request, f'Entry allowed for 1 year, e.g 20{actual_year}!')
                    return redirect(reverse('staff_details', args=[staff_id]))
                elif annual.end_date<annual.start_date:
                    messages.error(request, 'Start date Incorrect')
                    return redirect(reverse('staff_details', args=[staff_id]))              
                elif actual_year != annual_start_year and actual_year != annual_end_year:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x)) 
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))                                                      
                        for x in range (0,(annual.end_date-annual.start_date).days+1):                        
                            if (annual.start_date + datetime.timedelta(days = x)) in day_list:                            
                                count += 1                           
                            else:
                                count += 0                                          
                        if count !=0:
                            messages.error(request, 'Error Duplicate dates!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                        else:                            
                            difference = (annual.end_date - annual.start_date).days + 1           
                            annual.staff = staff
                            annual.days = difference
                            annual.save()                    
                            messages.success(request, 'Annnual leave added!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                    else:                        
                        difference = (annual.end_date - annual.start_date).days + 1                               
                        staff.save()                                     
                        annual.staff = staff
                        annual.days = difference
                        annual.save()                    
                        messages.success(request, 'Annual leave added!')
                        return redirect(reverse('staff_details', args=[staff_id]))
                else:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x)) 
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))                                                      
                        for x in range (0,(annual.end_date-annual.start_date).days+1):                        
                            if (annual.start_date + datetime.timedelta(days = x)) in day_list:                            
                                count += 1                           
                            else:
                                count += 0                                          
                        if count !=0:
                            messages.error(request, 'Error Duplicate dates!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                        else:                            
                            difference = (annual.end_date - annual.start_date).days + 1                                       
                            staff.annual_leave_remaining = staff.annual_leave_remaining - difference 
                            staff.save()                                     
                            annual.staff = staff
                            annual.days = difference
                            annual.save()                    
                            messages.success(request, 'Annnual leave added!')
                            return redirect(reverse('staff_details', args=[staff_id]))
                    else:                        
                        difference = (annual.end_date - annual.start_date).days + 1                                       
                        staff.annual_leave_remaining = staff.annual_leave_remaining - difference 
                        staff.save()                                     
                        annual.staff = staff
                        annual.days = difference
                        annual.save()                    
                        messages.success(request, 'Annual leave added!')
                        return redirect(reverse('staff_details', args=[staff_id]))
            else:                
                messages.error(
                    request, 'Sick leave could not be added. \
                        Please ensure the form is invalid.')
                return redirect(reverse('staff_details', args={staff_id}))
        else:          
            form = add_annual_leaveForm(instance=staff)
            context = {
                'form': form,
                'staff': staff,
            }
    return render(request, 'staff/annual_leave.html', context)


def sick_leave_taken(request, staff_id):
    """ A view for sick leave taken"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        if 'q' in request.GET:
            query = request.GET['q']
        else:
            query ='All'
        staff = get_object_or_404(Staff, id=staff_id)
        sick_leave = SickLeave.objects.all()
        if query == "All":
            sick_leave = sick_leave.filter(staff__id=staff_id).order_by('start_date') 
        else:
            sick_leave = sick_leave.filter(staff__id=staff_id, start_date__year=query).order_by('start_date') 
        actual_year = datetime.datetime.now().strftime("%y")
        context = {
            'staff': staff,
            'sick_leave': sick_leave,
            'year': query,
            'actual_year':actual_year,
        }        
        return render(request, 'staff/sick_leave_taken.html', context)


def annual_leave_taken(request, staff_id):
    """ A view for sick leave taken"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:        
        if 'q' in request.GET:
            query = request.GET['q']
        else:
            query="All"
        staff = get_object_or_404(Staff, id=staff_id)
        annual_leave = AnnualLeave.objects.all()
        if query == 'All':
            annual_leave = annual_leave.filter(staff__id=staff_id).order_by('start_date') 
        else:
            annual_leave = annual_leave.filter(staff__id=staff_id, start_date__year=query).order_by('start_date') 
        actual_year = datetime.datetime.now().strftime("%y")        
        context = {
            'staff': staff,
            'annual_leave': annual_leave,
            'actual_year': actual_year,
            'year': query,
        }        
        return render(request, 'staff/annual_leave_taken.html', context)


def sick_modify(request, sick_id):
    """ A view for sick leave taken"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        sick = get_object_or_404(SickLeave, id=sick_id)       
        staff = get_object_or_404(Staff, first_name=sick.staff.first_name)        
        original_difference = (sick.end_date - sick.start_date).days + 1        
        sick_leave_periods =  SickLeave.objects.all().filter(staff__id=staff.id).exclude(id=sick_id)
        annual_leave_periods =  AnnualLeave.objects.all().filter(staff__id=staff.id)              
        if request.method == 'POST':
            form = add_sick_leaveForm(request.POST, instance=sick)
            if form.is_valid():
                modified_sick = form.save(commit=False)
                actual_year = datetime.datetime.now().strftime("%y")
                sick_applied_year_start = modified_sick.start_date.strftime("%y")               
                sick_applied_year_end = modified_sick.end_date.strftime("%y")               
                if sick_applied_year_start != sick_applied_year_end:
                    messages.error(request, f'Entry allowed for 1 year only! e.g 20{actual_year}')
                    return redirect(reverse('sick_leave_taken', args=[sick.staff.id]))
                elif modified_sick.end_date<modified_sick.start_date:
                    messages.error(request, 'Start date Incorrect!')
                    return redirect(reverse('sick_leave_taken', args=[sick.staff.id]))
                elif actual_year != sick_applied_year_start and actual_year != sick_applied_year_end:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            sick_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, sick_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))
                        for leave in annual_leave_periods:
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
                            return redirect(reverse('sick_leave_taken', args=[sick.staff.id]))
                        else:                  
                            modified_difference = (modified_sick.end_date - modified_sick.start_date).days + 1
                            staff.save()
                            modified_sick.days = modified_difference                    
                            modified_sick.save()
                            return redirect(reverse('sick_leave_taken', args={sick.staff.id}))
                    else:
                        modified_difference = (modified_sick.end_date - modified_sick.start_date).days + 1             
                        staff.save()
                        modified_sick.days = modified_difference                    
                        modified_sick.save()
                        return redirect(reverse('sick_leave_taken', args={sick.staff.id}))
                else:                    
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in sick_leave_periods:
                            sick_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, sick_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))
                        for leave in annual_leave_periods:
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
                            return redirect(reverse('sick_leave_taken', args=[sick.staff.id]))
                        else:                          
                            modified_difference = (modified_sick.end_date - modified_sick.start_date).days + 1                 
                            staff.sick_leave_remaining = staff.sick_leave_remaining + original_difference - modified_difference 
                            staff.save()
                            modified_sick.days = modified_difference                    
                            modified_sick.save()
                            return redirect(reverse('sick_leave_taken', args={sick.staff.id}))
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


def annual_modify(request, annual_id):
    """ A view for sick leave taken"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        annual = get_object_or_404(AnnualLeave, id=annual_id)        
        staff = get_object_or_404(Staff, first_name=annual.staff.first_name)        
        original_difference = (annual.end_date - annual.start_date).days + 1        
        sick_leave_periods =  SickLeave.objects.all().filter(staff__id=staff.id)
        annual_leave_periods =  AnnualLeave.objects.all().filter(staff__id=staff.id).exclude(id=annual_id)              
        if request.method == 'POST':
            form = add_annual_leaveForm(request.POST, instance=annual)
            if form.is_valid():
                modified_annual = form.save(commit=False)
                actual_year = datetime.datetime.now().strftime("%y")
                annual_start_year = modified_annual.start_date.strftime("%y")                
                annual_end_year = modified_annual.end_date.strftime("%y")                
                if annual_start_year != annual_end_year:
                    messages.error(request, f'Entry allowed for 1 year only!. e.g 20{actual_year}')
                    return redirect(reverse('annual_leave_taken', args=[annual.staff.id]))
                elif modified_annual.end_date<modified_annual.start_date:
                    messages.error(request, 'Start date Incorrect!')
                    return redirect(reverse('annual_leave_taken', args=[annual.staff.id]))
                elif actual_year != annual_start_year and actual_year != annual_end_year:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))
                        for leave in sick_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))                                                        
                        for x in range (0,(modified_annual.end_date-modified_annual.start_date).days+1):                        
                            if (annual.start_date + datetime.timedelta(days = x)) in day_list:                            
                                count += 1                           
                            else:
                                count += 0                                          
                        if count !=0:
                            messages.error(request, 'Error Duplicate dates!')
                            return redirect(reverse('annual_leave_taken', args=[annual.staff.id]))
                        else:                        
                            modified_difference = (modified_annual.end_date - modified_annual.start_date).days + 1                 
                            staff.save()
                            modified_annual.days = modified_difference                    
                            modified_annual.save()
                            return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
                    else:
                        modified_difference = (modified_annual.end_date - modified_annual.start_date).days + 1                 
                        staff.save()
                        modified_annual.days = modified_difference                    
                        modified_annual.save()
                        return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
                else:
                    if sick_leave_periods or annual_leave_periods:
                        count =0
                        day_list = []
                        for leave in annual_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))
                        for leave in sick_leave_periods:
                            annual_days = (leave.end_date-leave.start_date).days + 1                        
                            for x in range(0, annual_days):
                                day_list.append(leave.start_date + datetime.timedelta(days = x))                                                        
                        for x in range (0,(modified_annual.end_date-modified_annual.start_date).days+1):                        
                            if (annual.start_date + datetime.timedelta(days = x)) in day_list:                            
                                count += 1                           
                            else:
                                count += 0                                          
                        if count !=0:
                            messages.error(request, 'Error Duplicate dates!')
                            return redirect(reverse('annual_leave_taken', args=[annual.staff.id]))
                        else:                        
                            modified_difference = (modified_annual.end_date - modified_annual.start_date).days + 1                 
                            staff.annual_leave_remaining = staff.annual_leave_remaining + original_difference - modified_difference 
                            staff.save()
                            modified_annual.days = modified_difference                    
                            modified_annual.save()
                            return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
                    else:
                        modified_difference = (modified_annual.end_date - modified_annual.start_date).days + 1                 
                        staff.annual_leave_remaining = staff.annual_leave_remaining + original_difference - modified_difference 
                        staff.save()
                        modified_annual.days = modified_difference                    
                        modified_annual.save()
                        return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
            else:
                messages.error(
                    request, 'Annual leave could not be modified. \
                        Please ensure the form is invalid.')
                return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
        else:          
            form = add_annual_leaveForm(instance=annual) 
            context = {
                'annual':annual,
                'form': form,            
            }        
        return render(request, 'staff/annual_modify.html', context)


def sick_delete(request, sick_id):
    """ A view to delete sick leave"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        actual_year = datetime.datetime.now().strftime("%y") 
        sick = get_object_or_404(SickLeave, id=sick_id)
        staff = get_object_or_404(Staff, first_name=sick.staff.first_name)
        if sick.start_date.strftime("%y") == actual_year:       
            staff.sick_leave_remaining = staff.sick_leave_remaining + sick.days
            staff.save()
            sick.delete()
            messages.success(request, 'Sick deleted!')
            return redirect(reverse('sick_leave_taken', args={sick.staff.id}))
        else:
            messages.success(request, 'Sick deleted!')
            sick.delete()
            return redirect(reverse('sick_leave_taken', args={sick.staff.id}))


def annual_delete(request, annual_id):
    """ A view to delete sick leave"""
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        actual_year = datetime.datetime.now().strftime("%y") 
        annual = get_object_or_404(AnnualLeave, id=annual_id)
        staff = get_object_or_404(Staff, first_name=annual.staff.first_name)
        if actual_year == annual.start_date.strftime("%y"):       
            staff.annual_leave_remaining = staff.annual_leave_remaining + annual.days
            staff.save()
            annual.delete()
            messages.success(request, 'Leave deleted!')
            return redirect(reverse('annual_leave_taken', args={annual.staff.id}))
        else:            
            annual.delete()
            messages.success(request, 'Leave deleted!')
            return redirect(reverse('annual_leave_taken', args={annual.staff.id}))


def sick_data(request):
    """ A view to send json sick data to template"""    
    if 'q' in request.GET:
        query = request.GET['q']
    else:
        query="All"
    
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        if query != 'All':
            all_sick = SickLeave.objects.all().filter(start_date__year=query).order_by('start_date')        
            sick_data = {'Jan':0, 'Feb':0, 'Mar':0, 'Apr':0, 'May':0, 'Jun':0, 'Jul':0, 'Aug':0, "Sep":0, 'Oct':0, 'Nov':0, "Dec":0}        
            for sick in all_sick:
                sick_month = sick.start_date                                 
                sick_data[sick_month.strftime("%b")]+=sick.days            
            json_data = json.dumps(sick_data)
            context = {
                'sick_data': json_data,
                'all_sick': all_sick,
                'year': query,                      
            }
            return render(request, 'staff/sick_data.html', context)
        else:
            all_sick = SickLeave.objects.all().order_by('start_date')
            json_data = {}       
            context = {                
                'all_sick': all_sick,
                'year': query,
                'sick_data': json_data,                   
            }
            return render(request, 'staff/sick_data.html', context)


def annual_leave_data(request):
    """ A view to send json leave data to template"""
        
    if 'q' in request.GET:        
        query = request.GET['q']
    else:
        query="All"       
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        if query != "All":             
            all_leave = AnnualLeave.objects.all().filter(start_date__year=query).order_by('start_date') 
            leave_data = {'Jan':0, 'Feb':0, 'Mar':0, 'Apr':0, 'May':0, 'Jun':0, 'Jul':0, 'Aug':0, "Sep":0, 'Oct':0, 'Nov':0, "Dec":0}        
            for leave in all_leave:
                leave_month = leave.start_date                                 
                leave_data[leave_month.strftime("%b")]+=leave.days            
            json_data = json.dumps(leave_data)
            context = {
                'leave_data': json_data,                
                'all_leave': all_leave,
                'year': query,                                    
            }
            return render(request, 'staff/leave_data.html', context)
        else:
            all_leave = AnnualLeave.objects.all().order_by('start_date')
            json_data = {}
            json_month_data = {}
            context = {
                'leave_data': json_data,
                'month_leave_data': json_month_data,               
                'all_leave': all_leave,
                'year': query,                                  
            }
            return render(request, 'staff/leave_data.html', context)


def leave_planner(request):
    """ A view to send json leave data to template"""    
    if 'q' in request.GET:       
        query = request.GET['q']
    else:
        query = '2021'
    if 'month' in request.GET:
        month = int(request.GET['month'])
    else:
        month=1       
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:       
        month_leave = AnnualLeave.objects.all().filter(start_date__month=month, start_date__year=query).order_by('start_date')
        month_dates = {}
        for x in range(1,32):
            month_dates[x]=0                     
        for leave in month_leave:
            start = int(leave.start_date.strftime("%d"))                      
            end = int(leave.end_date.strftime("%d"))
            if end < start:                
                end=monthrange(int(query), month)[1] 
            else:
                end = int(leave.end_date.strftime("%d"))                                        
            for x in range(start,end+1):
                month_dates[x]+=1               
        json_month_data = json.dumps(month_dates)      
        context = {        
            'month_leave_data': json_month_data,
            'year': query,
            'month': month, 
            'all_leave': month_leave,                   
        }
        return render(request, 'staff/leave_planner.html', context)

def sick_reset(request):
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        staff_sick = Staff.objects.all()
        actual_year = datetime.datetime.now().strftime("%Y")            
        for sick in staff_sick:
            total_sick = 0 
            total_sick_current_year = SickLeave.objects.all().filter(staff__id=sick.id, start_date__year=actual_year)
            for sick_days in total_sick_current_year:            
                total_sick += sick_days.days        
            sick.sick_leave_remaining = sick.sick_leave - total_sick
            sick.save()    
        return redirect(reverse('sick_data'))


def leave_reset(request):
    if not request.user.is_superuser:
            messages.error(request, 'Access Denied!')
            return redirect(reverse('home'))
    else:
        staff_leave = Staff.objects.all()
        actual_year = datetime.datetime.now().strftime("%Y")          
        for leave in staff_leave:
            total_leave = 0 
            total_leave_current_year = AnnualLeave.objects.all().filter(staff__id=leave.id, start_date__year=actual_year)
            for leave_days in total_leave_current_year:            
                total_leave += leave_days.days
            print(total_leave)        
            leave.annual_leave_remaining = leave.annual_leave - total_leave
            leave.save()         
        return redirect(reverse('annual_leave_data'))
