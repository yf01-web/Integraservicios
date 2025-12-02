from django.contrib import admin
from .models import User, Rol, PerfilUsuario


admin.site.register(PerfilUsuario)
admin.site.register(Rol)
