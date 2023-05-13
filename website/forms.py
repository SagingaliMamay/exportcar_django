from django import forms
from django .forms import ModelForm, CharField, TextInput, Textarea


from .models import *

#from multiupload.fields import MultiFileInput
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField



class Car_dataForm(ModelForm):
    class Meta:
        model = Car_data
        fields = '__all__'
        images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
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
            "photo": forms.FileInput(attrs={
                "multiple": True,
                'required': True,
            }),



    }

from django import forms

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


# Multiple files upload


from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

    # If you need to upload media files, you can use this:
'''  attachments = MultiMediaField(
        min_num=1,
        max_num=3,
        max_file_size=1024*1024*5,
        media_type='video'  # 'audio', 'video' or 'image'
    )

    # For images (requires Pillow for validation):
    attachments = MultiImageField(min_num=1, max_num=3, max_file_size=1024*1024*5)
    
'''

 