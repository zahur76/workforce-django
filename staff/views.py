from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Staff


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