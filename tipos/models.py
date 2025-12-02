from django.db import models
from unidades.models import UnidadServicio

class TipoRecurso(models.Model):
    idTipoRecurso = models.AutoField(primary_key=True)
    idUnidad = models.ForeignKey(UnidadServicio, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
