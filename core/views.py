from django.shortcuts import render, redirect
from django.contrib import messages  
from django.contrib.auth.models import User
from datetime import date
from recursos.models import Recurso
from tipos.models import TipoRecurso
from unidades.models import UnidadServicio
from usuarios.services import UsuarioService

#home pagina publica antes de iniciar sesion (login) donde se muestra el catalogo de algunos recursos que 
# presta el sistema interuniversitario IntegraServicios, es decir es una vista preliminar antes de loguearse

def home(request):
    """
    Página pública principal
    Si el usuario ya está autenticado, redirigir a su dashboard
    """
    # Si usuario ya está autenticado, redirigir a su dashboard
    if request.user.is_authenticated:
        # USAR SERVICIO
        return UsuarioService.redirigir_segun_rol(request.user)
    
    # Usuario NO autenticado - mostrar home público
    recursos_destacados = Recurso.objects.select_related(
        'idTipoRecurso',
        'idTipoRecurso__idUnidad'
    ).filter(
        estado='D'
    )[:6]
    
    tipos_recurso = TipoRecurso.objects.all()[:4]
    unidades = UnidadServicio.objects.all()[:3]
    
    context = {
        'recursos': recursos_destacados,
        'tipos_recurso': tipos_recurso,
        'unidades': unidades,
        'total_recursos': Recurso.objects.count(),
        'recursos_disponibles': Recurso.objects.filter(estado='D').count(),
    }
    
    return render(request, 'core/home.html', context)

# ===== VISTAS PÚBLICAS DE INFORMACIÓN =====

def about(request):
    """Página Acerca de"""
    return render(request, 'core/about.html')

def how_work(request):
    """Página Cómo funciona"""
    pasos = [
        {'numero': 1, 'titulo': 'Regístrate', 'descripcion': 'Crea una cuenta como cliente'},
        {'numero': 2, 'titulo': 'Explora recursos', 'descripcion': 'Busca recursos disponibles'},
        {'numero': 3, 'titulo': 'Reserva', 'descripcion': 'Selecciona fecha y hora'},
        {'numero': 4, 'titulo': 'Disfruta', 'descripcion': 'Usa el recurso en tu horario'},
    ]
    return render(request, 'core/how_work.html', {'pasos': pasos})

def contact(request):
    """Página de contacto"""
    return render(request, 'core/contact.html')


