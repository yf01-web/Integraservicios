"""
Decoradores para control de acceso por roles - Versión optimizada
"""
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .services import UsuarioService

def _verificar_autenticacion(request):
    """Función helper para verificar autenticación básica"""
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para acceder.")
        return False, redirect('login')
    
    if not UsuarioService.usuario_tiene_perfil(request.user):
        messages.error(request, "Tu perfil de usuario no está configurado.")
        return False, redirect('home')
    
    return True, None

def crear_decorador_rol(nombre_rol, propiedad_rol):
    """
    Factory function para crear decoradores de rol dinámicamente
    
    Args:
        nombre_rol: Nombre del rol para mensajes (ej: "clientes")
        propiedad_rol: Nombre de la propiedad (ej: "es_cliente")
    """
    def decorador_rol(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            # Verificar autenticación básica
            autenticado, respuesta = _verificar_autenticacion(request)
            if not autenticado:
                return respuesta
            
            # Verificar rol específico
            if not getattr(request.user.perfilusuario, propiedad_rol, False):
                messages.error(
                    request, 
                    f" Acceso restringido. Solo los {nombre_rol} pueden acceder aquí."
                )
                return UsuarioService.redirigir_segun_rol(request.user)
            
            # Usuario tiene permiso
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorador_rol

# Decoradores específicos usando la factory function
cliente_requerido = crear_decorador_rol("clientes", "es_cliente")
empleado_requerido = crear_decorador_rol("empleados", "es_empleado")
administrador_requerido = crear_decorador_rol("administradores", "es_administrador")

def cualquier_autenticado(view_func):
    """
    Decorador que permite acceso a cualquier usuario autenticado (cualquier rol).
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        autenticado, respuesta = _verificar_autenticacion(request)
        if not autenticado:
            return respuesta
        
        return view_func(request, *args, **kwargs)
    return wrapper