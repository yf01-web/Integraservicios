from django.db import models
from usuarios.models import PerfilUsuario
from reservas.models import Reserva

class Prestamo(models.Model):
    idPrestamo = models.AutoField(primary_key=True)
    idEmpleado = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    idReserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    horaEntrega = models.TimeField()

    def __str__(self):
        return f"Prestamo {self.idPrestamo} - Entregado por {self.idEmpleado.nombre_usuario}"
