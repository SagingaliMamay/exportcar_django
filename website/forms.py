from django import forms
from django .forms import ModelForm, CharField, TextInput, Textarea

from .models import *


class Car_dataForm(ModelForm):
    class Meta:
        model = Car_data
        fields = '__all__'

        widgets = {
        "mark": forms.TextInput(attrs={
                'class': 'form-control',
                'cols': 5, 'rows': 3,
                'placeholder':'Merk/Model:'
        }),
        "year": forms.TextInput(attrs={
            "class": 'form-control',
            "placeholder": 'Bouwjaar'
        }),
            "nrg": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Brandstof:'
            }),
            "transmission": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Transmissie'
            }),
            "km": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Kilometers'
            }),
            "price": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Prijs'
            }),
            "description": forms.Textarea(attrs={
                "class": 'form-control',
                "placeholder": 'Beschrijving:'

            }),
            "email": forms.EmailInput(attrs={
                "class": 'form-control',
                "placeholder": 'email'
            }),
            "name": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Naam'
            }),
            "tel": forms.TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Telefon'
            }),


    }





