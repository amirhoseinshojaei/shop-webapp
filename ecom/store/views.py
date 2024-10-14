from django.shortcuts import render, redirect
from .models import Product, User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})


def about(request):
    return render(request, 'store/about.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    else:

        return render(request, 'store/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('index')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        # Create the user
        user = User.objects.create(
            username=username,
            email=email,
            phone_number=phone,
            password=make_password(password)  # Password should be hashed
        )
        user.save()

        messages.success(request, 'User created successfully! Please log in.')
        return redirect('login')
    else:
        return render(request, 'store/register.html')
