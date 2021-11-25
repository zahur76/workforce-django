from django.shortcuts import get_object_or_404, render, redirect, reverse
from staff.models  import Staff
from django.contrib import messages
from django.db.models import Q


# Create your views here
def pay(request):
    """ A view to return the main pay management page """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    elif 'q' in request.GET:
        query = request.GET['q']
        if not query:
            return redirect(reverse('pay'))
        else:
            all_staff = Staff.objects.all()
            queries = Q(first_name__icontains=query) | Q(last_name__icontains=query)
            query_staff = all_staff.filter(queries)
            context = {
                'staff': query_staff,
            }
            return render(request, 'pay_management/pay.html', context)
    else:
        staff = Staff.objects.all()
        context = {
            'staff': staff,
        }

    return render(request, 'pay_management/pay.html', context)


def add_salary(request, staff_id):
    """ A view to return the main pay management page """
    if not request.user.is_superuser:
        messages.error(request, 'Permision Denied!.')
        return redirect(reverse('home'))

    staff = get_object_or_404(Staff, id=staff_id)
    context =  {
        'staff': staff,
    }

    return render(request, 'pay_management/add_salary.html', context)
