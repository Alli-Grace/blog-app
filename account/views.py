
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


# Create your views here.
def get_members(request):
    members = CustomUser.objects.all()
    return render(request, 'members.html', {'members':members})

def signup_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.create_user(
            first_name = first_name,
            email=email,
            password=password
        )
        # is_member = True
        user.save()
        login(request, user)
        messages.success(request, 'Signup successful')
        return redirect('login')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            print('Auth user', user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out")
    return redirect('login')

