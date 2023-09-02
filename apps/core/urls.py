from django.urls import path
from .views import home, cars, about, services, contact, login, signup


urlpatterns = [
    path('', home, name='home'),
    path('cars/', cars, name='cars'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
