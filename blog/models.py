from django.db import models
from djrichtextfield.models import RichTextField


# Create your models here.

# EXAMPLE OF RICHTEXTFIELD USE
# class Post(models.Model):
#     content = RichTextField(NULL, FALSE, ETC)

class NGO(models.Model):
    geo = [
        ('Local', 'Local'),
        ('Regional', 'Regional'),
        ('Multiregional', 'Multiregional'),
        ('National', 'National'),
        ('International', 'International'),
    ]
    categ = [
        ('Children', 'Children'),
        ('Elderly', 'Elderly'),
        ('Environmental', 'Environmental'),
        ('Education', 'Education'),
    ]
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    category = models.CharField(max_length=20, choices=categ, null=False, blank=False)
    location = models.CharField(max_length=60, unique=True, null=False, blank=False)
    geo_extend = models.CharField(max_length=20, choices=geo, null=False, blank=False)
    description = RichTextField(null=False)
    phone = models.IntegerField()
    email = models.EmailField(max_length=60, unique=True, null=False, blank=False)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    ngo = models.ForeignKey(NGO, related_name="event", on_delete=models.CASCADE)
    name =  models.CharField(max_length=100, unique=True, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    description = RichTextField(null=False)
    contact = models.CharField(max_length=60, unique=True, null=False, blank=False)

    def __str__(self):
        return f'Event {self.name} by {self.ngo}'