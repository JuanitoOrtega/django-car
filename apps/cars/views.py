from django.shortcuts import render, get_object_or_404
from .models import Car


# Create your views here.
def cars(request):
    context = {
        'title': 'Cars',
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'title': car.title,
        'car': car,
    }
    return render(request, 'cars/car_detail.html', context)