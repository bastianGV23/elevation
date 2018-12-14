from django import forms
from .models import Orden
from django import forms
from apps.core.models import User
from apps.clientes.models import Cliente

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ('nombreReceptor', 'cliente','id_ascensor','piezas','reparaciones','fallas','modelo_asc','email')
        widgets = {
        'nombreReceptor': forms.TextInput(attrs={'class': 'form-control '}),
        'cliente': forms.Select(attrs={'class': 'form-control '}),
        'id_ascensor': forms.TextInput(attrs={'class': 'form-control '}),
        'piezas': forms.TextInput(attrs={'class': 'form-control '}),
        'reparaciones': forms.TextInput(attrs={'class': 'form-control '}),
        'fallas': forms.TextInput(attrs={'class': 'form-control '}),
        'modelo_asc': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control '}),
    }
