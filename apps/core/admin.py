from django.contrib import admin

from .models import Team
from django.utils.html import format_html


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        alt_text = obj.get_fullname()
        return format_html('<img src="{}" width="35" style="border-radius: 5px;" alt="{}" />'.format(obj.photo.url, alt_text))

    thumbnail.short_description = 'Foto'

    list_display = ['id', 'thumbnail', 'get_fullname', 'designation', 'created_at']
    list_display_links = ['id', 'thumbnail', 'get_fullname']
    search_fields = ['first_name', 'last_name', 'designation']
    list_filter = ['designation']


# Register your models here.
admin.site.register(Team, TeamAdmin)
