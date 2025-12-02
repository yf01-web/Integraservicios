from django.db import models
from tipos.models import TipoRecurso

class Disponibilidad(models.Model):
    DIAS = [
        ('LU', 'Lunes'),
        ('MA', 'Martes'),
        ('MI', 'Miércoles'),
        ('JU', 'Jueves'),
        ('VI', 'Viernes'),
        ('SA', 'Sábado'),
        ('DO', 'Domingo'),
    ]

    idDisponibilidad = models.AutoField(primary_key=True)
    idTipoRecurso = models.ForeignKey(TipoRecurso, on_delete=models.CASCADE)

    diaSemana = models.CharField(max_length=2, choices=DIAS)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

    def __str__(self):
        return f"{self.idTipoRecurso.nombre} [{self.get_diaSemana_display()}]"
