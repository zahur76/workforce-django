from django.shortcuts import render

# Create your views here.
# Create your views here
def pay(request):
    """ A view to return the main pay management page """
    
    return render(request, 'pay_management/pay.html')
