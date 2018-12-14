from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.core.models import User

class userForm(UserCreationForm):
 class Meta:
    model = User
    fields = ('username','email','first_name','last_name','direccion')
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control '}),
        'email': forms.TextInput(attrs={'class': 'form-control','type':'email'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control '}),
        'last_name': forms.TextInput(attrs={'class': 'form-control '}),
        'direccion': forms.TextInput(attrs={'class': 'form-control '}),
    }

    """ USAR ESTO SI ES QUE SE REQUIERE USAR UNA VALIDACIÓN CUSTOMIZADA
    def clean(self):
        cleaned_data = super().clean()
        Rut = cleaned_data.get("rut")
        validaRut = Cliente.objects.filter(rut=Rut).exists()
        pNombre = cleaned_data.get("pNombre")
        if not len(Rut) == 9 :
                raise forms.ValidationError(
                    "El numero tiene que ser igual a 9"
                )
        if len(pNombre) <= 1:
            raise forms.ValidationError(
                "Debe ingresar un primer nombre"
            )
        if validaRut:
            raise forms.ValidationError(
                "El rut ingresado ya existe"
            )"""
