from django.db import models
from tipos.models import TipoRecurso

class Recurso(models.Model):
    ESTADOS = [
        ('D', 'Disponible'),
        ('O', 'Ocupado'),
        ('M', 'Mantenimiento'),
    ]

    idRecurso = models.AutoField(primary_key=True)
    idTipoRecurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='recursos/', null=True, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='D')

    def __str__(self):
        return self.nombre
