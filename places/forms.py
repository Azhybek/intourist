from django import forms
from django.db import models
from django.db.models import fields
from django.views.generic.edit import FormView
from .models import Feedback, Place

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'location', 'description']

class FeedbackFormView(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('place', 'text')