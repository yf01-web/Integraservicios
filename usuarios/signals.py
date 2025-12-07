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

# Crear perfil automáticamente cuando se crea un usuario
@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Si el usuario no tiene perfil, crear uno
        if not hasattr(instance, 'perfilusuario'):
            rol_cliente, _ = Rol.objects.get_or_create(nombre="Cliente")  
            PerfilUsuario.objects.create(
                user=instance,
                identification="",
                cellphonenumber="",
                rol=rol_cliente
            )

# Guardar el perfil cuando se actualiza el usuario
@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    if hasattr(instance, 'perfilusuario'):
        instance.perfilusuario.save()
