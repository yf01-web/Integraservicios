from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import PerfilUsuario, Rol
from .forms import RegistroForm
from django.contrib.auth import logout
from .decorators import cliente_requerido, empleado_requerido, administrador_requerido
from django.contrib.auth.decorators import login_required
from .services import UsuarioService


#-------------------------------------------------------------------------------------------------------------------

#para el registro, login, y logiut

#-------------------------------------------------------------------------------------------------------------------

def register_view(request):

    if request.method == "POST":

        form = RegistroForm(request.POST)

        if form.is_valid():
            identification = form.cleaned_data.get("identification")
            cellphonenumber = form.cleaned_data.get("cellphonenumber")

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                password=form.cleaned_data["password1"]
            )

            # Obtener el perfil creado automáticamente por la señal
            perfil = user.perfilusuario
            perfil.identification = identification
            perfil.cellphonenumber = cellphonenumber

            # Rol por defecto = Cliente (ya asignado por la señal)
            perfil.save()

            messages.success(request, "Cuenta creada correctamente.")
            return redirect("login")

    else:
        form = RegistroForm()

    return render(request, "usuarios/register.html", {"form": form})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                
                # USAR SERVICIO
                return UsuarioService.redirigir_segun_rol(user)
                
            else:
                messages.error(request, "Tu cuenta está inactiva.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "usuarios/login.html")



def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('home')


#--------------------------------------------------------------------------------------------------------------------

# para los decoradores

#--------------------------------------------------------------------------------------------------------------------

# ================================
# DASHBOARDS POR ROL (HOMES)
# ================================

@login_required
def dashboard_redirigir(request):
    """
    Redirige al usuario a su dashboard correspondiente según su rol.
    """
    # USAR SERVICIO
    return UsuarioService.redirigir_segun_rol(request.user)


@administrador_requerido
def dashboard_admin(request):
    """
    HOME para administradores - Vista principal después de login
    """
    from django.contrib.auth.models import User
    from recursos.models import Recurso
    
    context = {
        'total_usuarios': User.objects.count(),
        'total_recursos': Recurso.objects.count(),
        'total_reservas_hoy': 0,  # Implementar después
        'total_prestamos_activos': 0,  # Implementar después
    }
    return render(request, 'usuarios/dashboard_admin.html', context)


@empleado_requerido
def dashboard_empleado(request):
    """
    HOME para empleados - Vista principal después de login
    """
    context = {
        'reservas_pendientes': 0,
        'prestamos_activos': 0,
        'devoluciones_pendientes': 0,
    }
    return render(request, 'usuarios/dashboard_empleado.html', context)


@cliente_requerido
def dashboard_cliente(request):
    """
    HOME para clientes - Vista principal después de login
    """
    from recursos.models import Recurso
    
    # Recursos recomendados para el cliente
    recursos_recomendados = Recurso.objects.filter(
        estado='D'
    ).select_related('idTipoRecurso')[:4]
    
    context = {
        'recursos_recomendados': recursos_recomendados,
        'mis_reservas_activas': 0,
        'mis_reservas_pasadas': 0,
    }
    return render(request, 'usuarios/dashboard_cliente.html', context)