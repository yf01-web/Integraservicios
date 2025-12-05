# usuarios/services.py
"""
Servicios y helpers relacionados con usuarios
"""
from django.shortcuts import redirect

class UsuarioService:
    """
    Servicio para operaciones comunes de usuario
    """
    
    @staticmethod
    def obtener_redirect_segun_rol(usuario):
        """
        Retorna la URL de redirección según el rol del usuario
        
        Args:
            usuario: Objeto User de Django
            
        Returns:
            str: Nombre de la URL a redirigir
        """
        if not hasattr(usuario, 'perfilusuario'):
            return 'home'  # No tiene perfil, redirigir al home
        
        if usuario.perfilusuario.es_administrador:
            return 'dashboard_admin'
        elif usuario.perfilusuario.es_empleado:
            return 'dashboard_empleado'
        elif usuario.perfilusuario.es_cliente:
            return 'dashboard_cliente'
        else:
            return 'home'  # Rol no reconocido
    
    @staticmethod
    def redirigir_segun_rol(usuario):
        """
        Retorna un objeto redirect según el rol del usuario
        """
        url_name = UsuarioService.obtener_redirect_segun_rol(usuario)
        return redirect(url_name)
    
    @staticmethod  
    def usuario_tiene_perfil(usuario):
        """Verifica si el usuario tiene perfil configurado"""
        return hasattr(usuario, 'perfilusuario')
    
    @staticmethod
    def obtener_rol_display(usuario):
        """Retorna el nombre del rol para mostrar"""
        if not UsuarioService.usuario_tiene_perfil(usuario):
            return "Sin rol"
        
        if usuario.perfilusuario.es_administrador:
            return "Administrador"
        elif usuario.perfilusuario.es_empleado:
            return "Empleado"
        elif usuario.perfilusuario.es_cliente:
            return "Cliente"
        return "Sin rol definido"