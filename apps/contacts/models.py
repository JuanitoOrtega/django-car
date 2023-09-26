from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Nombres')
    last_name = models.CharField(max_length=255, verbose_name='Apellidos')
    car_id = models.IntegerField(verbose_name='ID del auto')
    car_title = models.CharField(max_length=255, verbose_name='Nombre del auto')
    car_price = models.IntegerField(verbose_name='Precio del auto')
    customer_need = models.CharField(max_length=255, verbose_name='Asunto')
    city = models.CharField(max_length=255, verbose_name='Ciudad')
    state = models.CharField(max_length=255, verbose_name='Departamento')
    email = models.EmailField(verbose_name='Correo electrónico')
    phone = models.CharField(max_length=12, blank=True, verbose_name='Teléfono')
    message = models.TextField(blank=True, verbose_name='Teléfono')
    user_id = models.IntegerField(verbose_name='ID de usuario')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Fecha')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.email
