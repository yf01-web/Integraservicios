from django.db import models
from usuarios.models import PerfilUsuario
from recursos.models import Recurso

class Reserva(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('C', 'Confirmada'),
        ('X', 'Cancelada'),
        ('E', 'En uso'),
        ('F', 'Finalizada'),
    ]

    idReserva = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    idRecurso = models.ForeignKey(Recurso, on_delete=models.CASCADE)

    fecha = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')

    def __str__(self):
        def __str__(self):
            return f"Reserva {self.idReserva} - {self.idUsuario.nombre_usuario} - {self.idRecurso.nombre}"
