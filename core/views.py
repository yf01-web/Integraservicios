from django.shortcuts import render, redirect
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from recursos.models import Recurso
from tipos.models import TipoRecurso
from unidades.models import UnidadServicio
from .decorators import cliente_requerido, empleado_requerido, administrador_requerido

#home pagina publica antes de iniciar sesion (login) donde se muestra el catalogo de algunos recursos que 
# presta el sistema interuniversitario IntegraServicios, es decir es una vista preliminar antes de loguearse

def home(request):
    """
    Página pública principal - muestra recursos destacados
    """
    # Obtener 6 recursos disponibles para mostrar
    recursos_destacados = Recurso.objects.select_related(
        'idTipoRecurso',
        'idTipoRecurso__idUnidad'
    ).filter(
        estado='D'  # Solo disponibles
    )[:6]  # Limitar a 6
    
    # Obtener tipos de recursos para el filtro
    tipos_recurso = TipoRecurso.objects.all()[:4]
    
    # Obtener unidades de servicio
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


