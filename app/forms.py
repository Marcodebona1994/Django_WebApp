from django import forms
from .models import BOP , PLSA


class BopForm(forms.ModelForm):
    class Meta:
        model = BOP
        fields = ['topn', 'DictSize','data', 'ppm']


class PlsaForm(forms.ModelForm):
    class Meta:
        model = PLSA
        fields = ['topic', 'topn', 'DictSize','data', 'ppm']