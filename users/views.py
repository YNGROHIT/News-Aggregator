from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Register View
def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if email or phone already exists in the database
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        if CustomUser.objects.filter(phone=phone).exists():
            messages.error(request, "Phone number already exists")
            return redirect('register')

        # Create new user
        try:
            user = CustomUser.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                country=country,
                password=password
            )
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')

    return render(request, 'users/register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user using the custom backend
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, "Invalid credentials, please try again.")
            return redirect('login')

    return render(request, 'users/login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out successfully.")
    return redirect('index')

def index(request):
    # If the user is logged in, redirect to home page
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'users/index.html')

@login_required
def home(request):
    return render(request, 'users/home.html')
