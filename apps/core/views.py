from django.shortcuts import render

from .models import Team


# Create your views here.
def home(request):
    teams = Team.objects.all()
    context = {
        'title': 'Welcome',
        'teams': teams
    }
    return render(request, 'pages/home.html', context)


def cars(request):
    context = {
        'title': 'Cars',
    }
    return render(request, 'pages/cars.html', context)


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
