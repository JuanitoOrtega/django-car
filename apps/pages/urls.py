from django.urls import path
from .views import home, about, services, contact, login, signup


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
]
