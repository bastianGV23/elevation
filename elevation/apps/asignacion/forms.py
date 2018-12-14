from django import forms
from .models import Asignacion
from django import forms
from apps.core.models import User

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('cli', 'tecnico',)
        widgets = {
        'cli': forms.Select(attrs={'class': 'form-control '}),
        'tecnico': forms.Select(attrs={'class': 'form-control'}),
    }

    def __init__(self,  *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
        self.fields['tecnico'].queryset = User.objects.filter(is_staff=False)