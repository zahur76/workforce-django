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
    """ A view to return staff details """
    form = add_staffForm()

    context = {
        'form': form,        
        }    
    
    return render(request, 'staff/add_staff.html', context)