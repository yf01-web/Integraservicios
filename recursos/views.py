from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from usuarios.decorators import administrador_requerido
from .models import Recurso
from .forms import RecursoForm

@administrador_requerido
def listar_recursos(request):
    recursos = Recurso.objects.select_related('idTipoRecurso', 'idTipoRecurso__idUnidad').all()
    return render(request, "recursos/listar_recursos.html", {"recursos": recursos})

@administrador_requerido
def crear_recurso(request):
    if request.method == "POST":
        form = RecursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Recurso creado correctamente.")
            return redirect("listar_recursos")
    else:
        form = RecursoForm()
    return render(request, "recursos/crear_recurso.html", {"form": form})

@administrador_requerido
def editar_recurso(request, idRecurso):
    recurso = get_object_or_404(Recurso, pk=idRecurso)
    if request.method == "POST":
        form = RecursoForm(request.POST, request.FILES, instance=recurso)
        if form.is_valid():
            form.save()
            messages.success(request, "Recurso actualizado correctamente.")
            return redirect("listar_recursos")
    else:
        form = RecursoForm(instance=recurso)
    return render(request, "recursos/editar_recurso.html", {"form": form, "recurso": recurso})

@administrador_requerido
def eliminar_recurso(request, idRecurso):
    recurso = get_object_or_404(Recurso, pk=idRecurso)
    # opcional: borrar archivo anterior físicamente si existe
    if recurso.foto:
        try:
            recurso.foto.delete(save=False)
        except:
            pass
    recurso.delete()
    messages.success(request, "Recurso eliminado correctamente.")
    return redirect("listar_recursos")
