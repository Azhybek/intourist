from django import forms
from django.db import models
from .models import Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description']