from django import forms
from .models import TipoRecurso

class TipoRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoRecurso
        fields = ['idUnidad', 'nombre', 'descripcion']
