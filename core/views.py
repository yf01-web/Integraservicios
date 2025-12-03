from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from recursos.models import Recurso
from .decorators import cliente_requerido, empleado_requerido, administrador_requerido

# Ejemplo de vista solo para clientes
@cliente_requerido
def nueva_reserva(request):
    return render(request, 'core/nueva_reserva.html')

# Ejemplo de vista solo para empleados  
@empleado_requerido
def registrar_prestamo(request):
    return render(request, 'core/registrar_prestamo.html')

# Ejemplo de vista solo para administradores
@administrador_requerido
def gestion_usuarios(request):
    return render(request, 'core/gestion_usuarios.html')


#home pagina publica antes de iniciar sesion (login) donde se muestra el catalogo de algunos recursos que 
# presta el sistema interuniversitario IntegraServicios, es decir es una vista preliminar antes de loguearse

def home(request):
    recursos = Recurso.objects.all()[:8]  # mostrar solo 8 recursos en portada
    context = {
        'recursos': recursos
    }
    return render(request, 'core/home.html', context)


