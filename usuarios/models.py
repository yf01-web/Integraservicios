from django.db import models
from django.contrib.auth.models import User

class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField(max_length=20)
    cellphonenumber = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username

    @property
    def es_cliente(self):
        return self.rol and self.rol.nombre == "Cliente"
    
    @property
    def es_empleado(self):
        return self.rol and self.rol.nombre == "Empleado"
    
    @property
    def es_administrador(self):
        return self.rol and self.rol.nombre == "Administrador"
    
    @property
    def tipo_rol(self):
        """Para usar en templates o lógica"""
        if self.es_administrador:
            return "administrador"
        elif self.es_empleado:
            return "empleado"
        elif self.es_cliente:
            return "cliente"
        return "sin_rol"


