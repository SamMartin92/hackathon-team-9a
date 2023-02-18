from django.contrib import admin
from .models import NGO, Event

# Register your models here.


@admin.register(NGO)
class NGO(admin.ModelAdmin):
    list_filter = ('category', 'location')
    search_fields = ['category', 'location', 'name']
    list_display = ('name', 'category', 'location', 'description', 'geo_extend', 'phone', 'email', 'website')


@admin.register(Event)
class Event(admin.ModelAdmin):
    list_filter = ('ngo', 'date')
    list_display = ('ngo', 'name', 'date', 'description', 'contact')
    search_fields = ['name', 'ngo']