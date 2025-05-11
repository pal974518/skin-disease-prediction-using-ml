from django import forms
from .models import SkinImage

class SkinImageForm(forms.ModelForm):
    class Meta:
        model = SkinImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }
