"""
Decoradores para control de acceso por roles
"""
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def cliente_requerido(view_func):
    """
    Decorador que restringe el acceso solo a usuarios con rol Cliente.
    
    Uso:
    @cliente_requerido
    def mi_vista(request):
        # Solo clientes pueden ver esta vista
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar autenticación
        if not request.user.is_authenticated:
            messages.error(request, "🔐 Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
        
        # Verificar que tenga perfil
        if not hasattr(request.user, 'perfilusuario'):
            messages.error(request, "⚠️ Tu perfil de usuario no está configurado correctamente.")
            return redirect('home')
        
        # Verificar que sea cliente
        if not request.user.perfilusuario.es_cliente:
            messages.error(request, "⛔ Acceso restringido. Solo los clientes pueden acceder aquí.")
            return redirect('home')
        
        # Usuario es cliente, permitir acceso
        return view_func(request, *args, **kwargs)
    return wrapper


def empleado_requerido(view_func):
    """
    Decorador que restringe el acceso solo a usuarios con rol Empleado.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "🔐 Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
        
        if not hasattr(request.user, 'perfilusuario'):
            messages.error(request, "⚠️ Tu perfil de usuario no está configurado correctamente.")
            return redirect('home')
        
        if not request.user.perfilusuario.es_empleado:
            messages.error(request, "⛔ Acceso restringido. Solo los empleados pueden acceder aquí.")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def administrador_requerido(view_func):
    """
    Decorador que restringe el acceso solo a usuarios con rol Administrador.
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "🔐 Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
        
        if not hasattr(request.user, 'perfilusuario'):
            messages.error(request, "⚠️ Tu perfil de usuario no está configurado correctamente.")
            return redirect('home')
        
        if not request.user.perfilusuario.es_administrador:
            messages.error(request, "⛔ Acceso restringido. Solo los administradores pueden acceder aquí.")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def cualquier_autenticado(view_func):
    """
    Decorador que permite acceso a cualquier usuario autenticado (cualquier rol).
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "🔐 Debes iniciar sesión para acceder a esta página.")
            return redirect('login')
        
        if not hasattr(request.user, 'perfilusuario'):
            messages.error(request, "⚠️ Tu perfil de usuario no está configurado correctamente.")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper