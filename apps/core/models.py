from django.db import models


# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Nombres')
    last_name = models.CharField(max_length=255, verbose_name='Apellidos')
    designation = models.CharField(max_length=255, verbose_name='Cargo')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Foto')
    facebook_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Facebook')
    twitter_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Twitter')
    instagram_link = models.URLField(max_length=255, blank=True, null=True, verbose_name='Instagram')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Registro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipo'

    def get_fullname(self):
        if self.first_name or self.last_name:
            return f'{self.first_name} {self.last_name}'

    get_fullname.short_description = 'Nombre completo'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'