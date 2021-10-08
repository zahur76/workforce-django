from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Staff
from .forms import add_staffForm


# Create your views here
def staff(request):
    """ A view to return staff info """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home')) 
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
        print(staff)
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