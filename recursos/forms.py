from django import forms
from .models import Recurso

class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso
        fields = ['idTipoRecurso', 'nombre', 'descripcion', 'foto', 'estado']
        labels = {
            'idTipoRecurso': 'Tipo de Recurso',
            'nombre': 'Nombre del Recurso',
            'descripcion': 'Descripción',
            'foto': 'Foto (opcional)',
            'estado': 'Estado',
        }
        widgets = {
            'idTipoRecurso': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # foto usará widget por defecto (FileInput). Si quieres estilo:
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }
