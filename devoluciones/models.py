from django.db import models
from usuarios.models import PerfilUsuario
from prestamos.models import Prestamo

class Devolucion(models.Model):
    idDevolucion = models.AutoField(primary_key=True)
    idPrestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    idEmpleado = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)

    horaDevolucion = models.TimeField()

    def __str__(self):
        return f"Devolución {self.idDevolucion} - Préstamo {self.idPrestamo.idPrestamo}"
