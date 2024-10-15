from django.shortcuts import render, redirect
from .models import Product, User, Category
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={'products': products})


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'store/product_details.html', context={'product': product})


def category_details(request, slug):
    # Replace Hyphens with spaces
    # foo = foo.replace('-', ' ')
    # Grab the Category from url
    try:
        # Look Up the Category
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category=category)

        # Fetch all categories for the navbar
        categories = Category.objects.all()
        return render(request, 'store/category_details.html', context={'categories': categories, 'category': category, 'products': products})
    except category.DoesNotExist:
        messages.error(request, 'Category does not exist')
        return redirect('index')


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
            phone=phone,
            password=make_password(password)  # Password should be hashed
        )
        user.save()

        messages.success(request, 'User created successfully!')
        login(request, user)
        return redirect('index')
    else:
        return render(request, 'store/register.html')
