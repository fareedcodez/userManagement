from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render (request, 'pages/index.html')


def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = {'form':form}
    
    return render(request, 'pages/register.html', context = context)

def login(request):
    return render(request, 'pages/login.html')

def logout(request):
    return render(request, 'pages/index.html')