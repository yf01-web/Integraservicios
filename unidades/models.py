from django.db import models

class UnidadServicio(models.Model):
    idUnidad = models.AutoField(primary_key=True)
    nombreUnidad = models.CharField(max_length=100)
    horarioInicio = models.TimeField()
    horarioFin = models.TimeField()
    granularidad = models.CharField(max_length=20)

    def __str__(self):
        return self.nombreUnidad
