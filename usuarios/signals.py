from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Rol, PerfilUsuario

# Crear roles después de migraciones
@receiver(post_migrate)
def crear_roles(sender, **kwargs):
    if sender.label == "usuarios":
        Rol.objects.get_or_create(nombre="Cliente")
        Rol.objects.get_or_create(nombre="Empleado")
        Rol.objects.get_or_create(nombre="Administrador")

