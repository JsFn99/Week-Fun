from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        if username is None or username == '':
            
            return render(request, 'accounts/signup.html', {'error': 'Please enter a valid username'})
        
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')