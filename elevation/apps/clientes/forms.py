from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from .models import Cliente

class clienteForm(forms.ModelForm):
 class Meta:
    model = Cliente
    fields = ('nombre','direccion','ciudad','comuna','email')
    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control '}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'ciudad': forms.TextInput(attrs={'class': 'form-control '}),
        'comuna': forms.TextInput(attrs={'class': 'form-control '}),
        'email': forms.TextInput(attrs={'class': 'form-control ','type':'email'}),
    }