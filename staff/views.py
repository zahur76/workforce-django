from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here
def staff(request):
    """ A view to return staff info """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home')) 

    
    return render(request, 'staff/staff.html')