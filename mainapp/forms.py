# converter/forms.py

from django import forms
from .models import Conversion

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Conversion
        fields = ['image']
