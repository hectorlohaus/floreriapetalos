from django import forms
from django.forms import ModelForm
from .models import Flor
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    pass

class FlorForm(ModelForm):
    valor= forms.IntegerField(min_value=0, max_value=100000)
    class Meta:
        model=Flor
        fields=['nombre','valor','descripcion','estado','stock','fotografia']


   