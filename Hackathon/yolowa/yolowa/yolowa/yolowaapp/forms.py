from django import forms
from .models import Yolowaapp

class YolowaappForm(forms.ModelForm):
    class Meta:
        model = Yolowaapp
        fields = ['title', 'body']
