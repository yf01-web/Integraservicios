from django.shortcuts import render, redirect
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date
from recursos.models import Recurso
from tipos.models import TipoRecurso
from unidades.models import UnidadServicio
from .decorators import cliente_requerido, empleado_requerido, administrador_requerido

# # Ejemplo de vista solo para clientes
# @cliente_requerido
# def nueva_reserva(request):
#     return render(request, 'core/nueva_reserva.html')

# # Ejemplo de vista solo para empleados  
# @empleado_requerido
# def registrar_prestamo(request):
#     return render(request, 'core/registrar_prestamo.html')

# # Ejemplo de vista solo para administradores
# @administrador_requerido
# def gestion_usuarios(request):
#     return render(request, 'core/gestion_usuarios.html')


#home pagina publica antes de iniciar sesion (login) donde se muestra el catalogo de algunos recursos que 
# presta el sistema interuniversitario IntegraServicios, es decir es una vista preliminar antes de loguearse

def home(request):
    """
    Página pública principal - muestra recursos destacados
    """
    # Obtener 6 recursos disponibles para mostrar
    recursos_destacados = Recurso.objects.select_related(
        'idTipoRecurso',
        'idTipoRecurso'
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


@login_required
def dashboard(request):
    """
    Dashboard según el rol del usuario
    Redirige a la vista específica de cada rol
    """
    if not hasattr(request.user, 'perfilusuario'):
        messages.error(request, "Tu perfil no está configurado correctamente.")
        return redirect('home')
    
    # Redirigir según rol
    if request.user.perfilusuario.es_administrador:
        return redirect('dashboard_admin')
    elif request.user.perfilusuario.es_empleado:
        return redirect('dashboard_empleado')
    elif request.user.perfilusuario.es_cliente:
        return redirect('dashboard_cliente')
    else:
        messages.error(request, "Rol no reconocido.")
        return redirect('home')


# ===== DASHBOARDS ESPECÍFICOS POR ROL =====

@administrador_requerido
def dashboard_admin(request):
    """Dashboard para administradores"""
    context = {
        'total_usuarios': User.objects.count(),
        'total_recursos': Recurso.objects.count(),
        'total_reservas_hoy': 0,  # Implementar después
        'total_prestamos_activos': 0,  # Implementar después
    }
    return render(request, 'core/dashboard_admin.html', context)


@empleado_requerido
def dashboard_empleado(request):
    """Dashboard para empleados"""
    # Obtener reservas para hoy (implementar después)
    # reservas_hoy = Reserva.objects.filter(fecha=date.today()).count()
    
    context = {
        'reservas_pendientes': 0,
        'prestamos_activos': 0,
        'devoluciones_pendientes': 0,
    }
    return render(request, 'core/dashboard_empleado.html', context)


@cliente_requerido
def dashboard_cliente(request):
    """Dashboard para clientes"""
    # Obtener reservas del usuario (implementar después)
    # mis_reservas = Reserva.objects.filter(usuario=request.user).count()
    
    # Recursos recomendados para el cliente
    recursos_recomendados = Recurso.objects.filter(
        estado='D'
    ).select_related('tipo_recurso')[:4]
    
    context = {
        'recursos_recomendados': recursos_recomendados,
        'mis_reservas_activas': 0,
        'mis_reservas_pasadas': 0,
    }
    return render(request, 'core/dashboard_cliente.html', context)


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


