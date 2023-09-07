from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    context = {
        'title': 'Iniciar sesión',
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Inicio de sesión exitoso!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales de acceso incorrectos!')
            return redirect('login')
    return render(request, 'users/login.html', context)


def signup(request):
    context = {
        'title': 'Registrarse',
    }
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya existe!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya existe!')
            else:
                User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                messages.success(request, 'Cuenta registrada exitosamente!')
                return redirect('login')
        else:
            messages.error(request, 'Las contraseñas ingresadas no coinciden!')
    return render(request, 'users/signup.html', context)


def dashboard(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'users/dashboard.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')