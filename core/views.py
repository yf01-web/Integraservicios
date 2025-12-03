from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from recursos.models import Recurso

#home pagina publica antes de iniciar sesion (login) donde se muestra el catalogo de algunos recursos que 
# presta el sistema interuniversitario IntegraServicios, es decir es una vista preliminar antes de loguearse

def home(request):
    recursos = Recurso.objects.all()[:8]  # mostrar solo 8 recursos en portada
    context = {
        'recursos': recursos
    }
    return render(request, 'core/home.html', context)


