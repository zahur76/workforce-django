from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render, reverse


# login view
def login_view(request):
    if request.method == "POST":
        """View to login as admin"""
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect(reverse("home"))
        else:
            # Return an 'invalid login' error message.
            messages.error(request, "Login Unsuccessful!")
            return redirect(reverse("home"))


def logout_view(request):
    """View to logout as admin"""
    logout(request)
    messages.success(request, "Logout Successful!")
    return redirect(reverse("home"))
