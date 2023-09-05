from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from django.db.models import Q


# Create your views here.
def cars(request):
    cars = Car.objects.all().order_by('-created_at')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')

    try:
        paged_cars = paginator.get_page(page)
    except EmptyPage:
        # Si la página solicitada está fuera del rango, redirecciona a la última página válida
        paged_cars = paginator.get_page(paginator.num_pages)
    except PageNotAnInteger:
        # Si la página solicitada no es un número válido, muestra la primera página
        paged_cars = paginator.get_page(1)

    conditions = Car.objects.order_by('condition').values_list('condition', flat=True).distinct()
    cities = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    years = Car.objects.order_by('-year').values_list('year', flat=True).distinct()
    body_styles = Car.objects.order_by('body_style').values_list('body_style', flat=True).distinct()
    transmissions = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()

    context = {
        'title': 'Cars',
        'cars': paged_cars,
        'conditions': conditions,
        'cities': cities,
        'years': years,
        'body_styles': body_styles,
        'transmissions': transmissions,
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    context = {
        'title': car.title,
        'car': car,
    }
    return render(request, 'cars/car_detail.html', context)


def search(request):
    cars = Car.objects.all().order_by('-created_at')

    brands = Car.objects.order_by('brand').values_list('brand', flat=True).distinct()
    models = Car.objects.order_by('model').values_list('model', flat=True).distinct()
    cities = Car.objects.order_by('city').values_list('city', flat=True).distinct()
    years = Car.objects.order_by('-year').values_list('year', flat=True).distinct()
    conditions = Car.objects.order_by('condition').values_list('condition', flat=True).distinct()
    transmissions = Car.objects.order_by('transmission').values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))

    if 'brand' in request.GET:
        brand = request.GET['brand']
        if brand:
            cars = cars.filter(brand__iexact=brand)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            cars = cars.filter(condition__iexact=condition)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price or min_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'title': 'Resultados de búsqueda',
        'brands': brands,
        'models': models,
        'cities': cities,
        'years': years,
        'conditions': conditions,
        'transmissions': transmissions,
        'cars': cars,
    }
    return render(request, 'cars/search.html', context)