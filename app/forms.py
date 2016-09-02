from django import forms

from .models import Height


class HeightForm(forms.Form):
    """This is a casual form"""
    cushion = forms.CharField(max_length=255)
    faucet = forms.CharField(max_length=255)


class HeightFormV2(forms.ModelForm):
    class Meta:
        model = Height
        fields = '__all__'
