from django import forms
from .models import Image

class ImageCreation(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url':forms.HiddenInput,
        }