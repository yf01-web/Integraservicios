from django.shortcuts import render, redirect
from usuarios.decorators import administrador_requerido
from .models import TipoRecurso
from .forms import TipoRecursoForm

@administrador_requerido
def listar_tipos(request):
    tipos = TipoRecurso.objects.all()
    return render(request, 'tipos/listar_tipos.html', {'tipos': tipos})

@administrador_requerido
def crear_tipo(request):
    if request.method == 'POST':
        form = TipoRecursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tipos')
    else:
        form = TipoRecursoForm()

    return render(request, 'tipos/crear_tipo.html', {'form': form})
