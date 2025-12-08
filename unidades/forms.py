from django import forms
from .models import UnidadServicio

class UnidadForm(forms.ModelForm):
    class Meta:
        model = UnidadServicio
        fields = ['nombreUnidad', 'horarioInicio', 'horarioFin', 'granularidad']

        widgets = {
            'nombreUnidad': forms.TextInput(attrs={'class': 'form-control'}),
            'horarioInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horarioFin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'granularidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
