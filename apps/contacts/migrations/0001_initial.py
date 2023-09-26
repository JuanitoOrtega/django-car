# Generated by Django 4.2.4 on 2023-09-16 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('car_id', models.IntegerField(verbose_name='ID del auto')),
                ('customer_need', models.CharField(max_length=255, verbose_name='Asunto')),
                ('car_title', models.CharField(max_length=255, verbose_name='Nombre del auto')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('state', models.CharField(max_length=255, verbose_name='Departamento')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('phone', models.CharField(max_length=12, verbose_name='Teléfono')),
                ('message', models.TextField(blank=True, verbose_name='Teléfono')),
                ('user_id', models.IntegerField(verbose_name='ID de usuario')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
    ]