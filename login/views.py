from django.http import HttpResponse,HttpResponseRedirect 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages #new line
from django.contrib.auth.models import User


# Show the login page
def home(request):
    return render(request, 'login/index.html')

# Handle login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('parent_dashboard:dashboard')  # Redirect to dashboard on success
        else:
            return render(request, 'login/index.html', {'error': 'Invalid credentials'})

    return render(request, 'login/index.html')

# Show the dashboard (after login)
@login_required
def dashboard(request):
    return render(request, 'parent_dashboard/dashboard.html')

# Handle logout new line
@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("login")  # Redirect to login page after logout

from django.shortcuts import render

def signup(request):
    # Your signup logic here
    return render(request, 'login/signup.html')  # Replace with your template
