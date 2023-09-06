from django.shortcuts import redirect, render
from django.contrib import messages


# Create your views here.
def login(request):
    context = {
        'title': 'Iniciar sesión',
    }
    return render(request, 'users/login.html', context)


def signup(request):
    context = {
        'title': 'Registrarse',
    }

    if request.method == 'POST':
        messages.error(request, 'Este es un mensaje de error')
        return redirect('signup')
    else:
        return render(request, 'users/signup.html', context)


def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'users/dashboard.html', context)


def logout(request):
    return redirect('home')