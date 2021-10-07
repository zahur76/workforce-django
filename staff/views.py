from django.shortcuts import render


# Create your views here
def staff(request):
    """ A view to return the index page """
    
    return render(request, 'staff/staff.html')