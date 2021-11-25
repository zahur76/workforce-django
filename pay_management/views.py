from django.shortcuts import get_object_or_404, render, redirect, reverse
from staff.models  import Staff
from django.contrib import messages
from django.db.models import Q
from .forms import add_salaryForm
import time
import json


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

    else:
        staff = get_object_or_404(Staff, id=staff_id)
        if request.method == 'POST':
            form = add_salaryForm(request.POST)
            if form.is_valid():
                salary = form.save(commit=False)
                salary.staff = staff
                salary.created_at = time.strftime("%Y%m%d-%H%M%S")
                salary.tax_number = staff.tax_number
                salary.gross_salary = salary.basic_salary + salary.transport_allowance + salary.non_taxable_additional_allowances + salary.taxable_additional_allowances
                salary.total_deduction = (salary.basic_salary + salary.taxable_additional_allowances) * (salary.tax_deduction/100)
                salary.net_salary = salary.gross_salary - salary.total_deduction
                salary_dictionary = {
                    'staff': staff.first_name + " " + staff.last_name,
                    'Created at': time.strftime("%Y%m%d-%H%M%S"),
                    'Basic Salary': salary.basic_salary,
                    'transport_allowance': salary.transport_allowance,
                    'non_taxable additional allowances': salary.non_taxable_additional_allowances,
                    'taxable additional allowances': salary.taxable_additional_allowances,
                    'tax deduction': salary.tax_deduction,
                    'gross salary':salary.gross_salary,
                    'total deduction': salary.total_deduction,
                    'net_salary':salary.net_salary,
                }
                salary.json_salary = json.dumps(salary_dictionary)
                salary.save()
                messages.success(request, 'Salary Added!')
                return redirect(reverse('staff_details', args=[staff_id]))
            else:
                messages.error(
                    request, 'Staff could not be added. \
                        Please ensure the form is valid.')
                return redirect(reverse('update_staff', args={staff_id}))

        form = add_salaryForm(instance=staff)
        context = {
            'form': form,
            'staff': staff,
            }
        return render(request, 'pay_management/add_salary.html', context)
