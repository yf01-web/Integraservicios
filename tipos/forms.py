from django import forms
from .models import TipoRecurso
from unidades.models import UnidadServicio

class TipoRecursoForm(forms.ModelForm):
    class Meta:
        model = TipoRecurso
        fields = ["nombre", "descripcion", "idUnidad"]
        labels = {
            "nombre": "Nombre del tipo de recurso",
            "descripcion": "Descripción",
            "idUnidad": "Unidad de Servicio",
        }
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "idUnidad": forms.Select(attrs={"class": "form-control"}),
        }
