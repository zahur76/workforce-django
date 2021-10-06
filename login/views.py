from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages


# login view
def login_view(request):
    if request.method == 'POST':
        print('zahur zahur') 
        ''' View to login as admin '''    
        username = request.POST['username']    
        password = request.POST['password']
        print(username)       
        user = authenticate(request, username=username, password=password)
        if user is not None:                 
            login(request, user)            
            messages.success(request, 'Login Successful!')
            return redirect(reverse('home'))
        else:
            # Return an 'invalid login' error message.        
            messages.error(request, 'Login Unsuccessful!')
            return redirect(reverse('home'))