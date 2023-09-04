from django.shortcuts import render

from apps.cars.models import Car
from .models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_at')
    latest_cars = Car.objects.all().order_by('-created_at')
    context = {
        'title': 'Welcome',
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        'title': 'Welcome',
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def services(request):
    context = {
        'title': 'Services',
    }
    return render(request, 'pages/services.html', context)


def contact(request):
    context = {
        'title': 'Contact',
    }
    return render(request, 'pages/contact.html', context)


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'pages/login.html', context)


def signup(request):
    context = {
        'title': 'Sign Up',
    }
    return render(request, 'pages/signup.html', context)
