from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):
    brands = (
        ('Audi', 'Audi'),
        ('Changan', 'Changan'),
        ('Ferrari', 'Ferrari'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('JAC', 'JAC'),
        ('Jaguar', 'Jaguar'),
        ('Kia', 'Kia'),
        ('Lamborghini', 'Lamborghini'),
        ('Nissan', 'Nissan'),
        ('Porche', 'Porche'),
        ('Renault', 'Renault'),
        ('Subaru', 'Subaru'),
        ('Suzuki', 'Suzuki'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
    )

    state_choice = (
	    ('BN', 'Beni'),
	    ('CB', 'Cochabamba'),
        ('CH', 'Chuquisaca'),
        ('LP', 'La Paz'),
	    ('OR', 'Oruro'),
        ('PN', 'Pando'),
        ('PT', 'Potosí'),
        ('TJ', 'Tarija'),
        ('SC', 'Santa Cruz'),
    )

    def get_state_name(self):
        for state_code, state_name in self.state_choice:
            if state_code == self.state:
                return state_name
        return ""

    year_choice = []
    for r in range(2010, (datetime.now().year+1)):
        year_choice.append((r,r))

    features_choices = (
        ('Control de crucero', 'Control de crucero'),
        ('Interfaz de audio', 'Interfaz de audio'),
        ('Airbags', 'Airbags'),
        ('Aire acondicionado', 'Aire acondicionado'),
        ('Calefacción de asientos', 'Calefacción de asientos'),
        ('Sistema de alarma', 'Sistema de alarma'),
        ('Asistente de estacionamiento', 'Asistente de estacionamiento'),
        ('Dirección asistida', 'Dirección asistida'),
        ('Cámara de retroceso', 'Cámara de retroceso'),
        ('Inyección directa de combustible', 'Inyección directa de combustible'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Deflector de viento', 'Deflector de viento'),
        ('Teléfono Bluetooth', 'Teléfono Bluetooth'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    title = models.CharField(max_length=255, verbose_name='Título')
    state = models.CharField(choices=state_choice, max_length=100, verbose_name='Departamento')
    city = models.CharField(max_length=100, verbose_name='Ciudad')
    brand = models.CharField(choices=brands, max_length=100, verbose_name='Marca')
    color = models.CharField(max_length=100, verbose_name='Color')
    model = models.CharField(max_length=100, verbose_name='Modelo')
    year = models.IntegerField(choices=year_choice, verbose_name='Año')
    condition = models.CharField(max_length=100, verbose_name='Condición')
    normal_price = models.IntegerField(blank=True, null=True, verbose_name='Precio regular')
    price = models.IntegerField(verbose_name='Precio')
    description = RichTextField(verbose_name='Descripción')
    photo = models.ImageField(upload_to='photos/cars/%Y/%m/%d/', verbose_name='Foto destacada')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 1')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 2')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 3')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Foto 4')
    features = MultiSelectField(choices=features_choices, max_choices=13, max_length=255, verbose_name='Características')
    body_style = models.CharField(max_length=100, verbose_name='Tipo')
    engine = models.CharField(max_length=100, verbose_name='Motor')
    transmission = models.CharField(max_length=100, verbose_name='Transmisión')
    interior = models.CharField(max_length=100, verbose_name='Interior')
    kilometres = models.IntegerField(verbose_name='Kilómetros')
    doors = models.CharField(choices=door_choices, max_length=10, verbose_name='Puertas')
    passengers = models.IntegerField(verbose_name='Pasajeros')
    vin_no = models.CharField(max_length=100, verbose_name='Chasis')
    kilometraje = models.IntegerField(verbose_name='Kilometraje')
    fuel_type = models.CharField(max_length=50, verbose_name='Combustible')
    no_of_owners = models.CharField(max_length=100, verbose_name='Propietarios')
    is_featured = models.BooleanField(default=False, verbose_name='Destacado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return self.title