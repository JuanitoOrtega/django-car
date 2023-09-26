from django.shortcuts import render, redirect

from apps.cars.models import Car
from .models import Team
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_at')
    latest_cars = Car.objects.all().order_by('-created_at')
    brands = Car.objects.order_by('brand').values_list('brand', flat=True).distinct()
    models = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    cities = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    years = Car.objects.order_by('-year').values_list('year', flat=True).distinct()
    body_styles = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    context = {
        'title': 'Welcome',
        'teams': teams,
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'brands': brands,
        'models': models,
        'cities': cities,
        'years': years,
        'body_styles': body_styles,
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
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'Tienes un nuevo mensaje desde tu sitio web Car, con el asunto: ' + subject
        message_body = 'Nombre: ' + full_name + '. Correo electrónico: ' + email + '. Teléfono: ' + phone + '. Mensaje: ' + message

        admin_info = User.objects.get(is_superuser=True)

        # Contact email
        send_mail(
            email_subject,
            message_body,
            "ortegaj83@gmail.com",
            [admin_info.email],
            fail_silently=False,
        )

        messages.success(request, 'Gracias por contactarnos, te responderemos tan pronto como podamos.')
        return redirect('contact')

    context = {
        'title': 'Contact',
    }

    return render(request, 'pages/contact.html', context)
