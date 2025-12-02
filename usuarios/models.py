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


# from django.db import models

# class Rol(models.Model):
#     idRol = models.AutoField(primary_key=True)
#     nombreROL = models.CharField(max_length=50)

#     def __str__(self):
#         return self.nombreROL


# class Usuario(models.Model):
#     idUsuario = models.BigAutoField(primary_key=True)
#     idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)

#     identificacion = models.CharField(max_length=20)      
#     nombre_usuario = models.CharField(max_length=50)
#     nombre = models.CharField(max_length=100)
#     correo = models.EmailField()
#     celular = models.BigIntegerField()
#     contraseña = models.CharField(max_length=128)

#     def __str__(self):
#         return self.nombre_usuario
