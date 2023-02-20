from djrichtextfield.widgets import RichTextWidget
from django import forms
from django.forms import fields, ModelForm
from .models import NGO, Event


# EXAMPLE OF RICHTEXTFIELD USE
class AddNGOForm(forms.ModelForm):

    class Meta:
        model = NGO
        fields = ('name', 'category', 'location', 'description', 'geo_extend', 'phone', 'email', 'website', 'image')
