from django.contrib import admin

from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        alt_text = obj.title
        return format_html('<img src="{}" width="35" style="border-radius: 5px;" alt="{}" />'.format(obj.photo.url, alt_text))

    thumbnail.short_description = 'Foto'

    list_display = ['thumbnail', 'title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured']
    list_display_links = ['thumbnail', 'title']
    search_fields = ['title', 'city', 'model', 'brand', 'body_style', 'fuel_type']
    list_filter = ['year', 'state', 'brand']
    list_editable = ['is_featured']


# Register your models here.
admin.site.register(Car, CarAdmin)
