from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TipoRecurso
from .forms import TipoRecursoForm
from usuarios.decorators import administrador_requerido


@administrador_requerido
def listar_tipos(request):
    tipos = TipoRecurso.objects.select_related("idUnidad").all()
    return render(request, "tipos/listar_tipos.html", {"tipos": tipos})


@administrador_requerido
def crear_tipo(request):
    if request.method == "POST":
        form = TipoRecursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de recurso creado correctamente.")
            return redirect("listar_tipos")
    else:
        form = TipoRecursoForm()

    return render(request, "tipos/crear_tipo.html", {"form": form})


@administrador_requerido
def editar_tipo(request, idTipoRecurso):
    tipo = get_object_or_404(TipoRecurso, pk=idTipoRecurso)

    if request.method == "POST":
        form = TipoRecursoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request, "Tipo de recurso actualizado.")
            return redirect("listar_tipos")
    else:
        form = TipoRecursoForm(instance=tipo)

    return render(request, "tipos/editar_tipo.html", {"form": form, "tipo": tipo})


@administrador_requerido
def eliminar_tipo(request, idTipoRecurso):
    tipo = get_object_or_404(TipoRecurso, pk=idTipoRecurso)
    tipo.delete()
    messages.success(request, "Tipo de recurso eliminado correctamente.")
    return redirect("listar_tipos")
