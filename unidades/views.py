from django.shortcuts import render, redirect
from .models import UnidadServicio
from .forms import UnidadForm
from django.contrib import messages

def listar_unidades(request):
    unidades = UnidadServicio.objects.all()
    return render(request, "unidades/listar_unidades.html", {
        "unidades": unidades
    })


def crear_unidad(request):
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidad de servicio creada correctamente.")
            return redirect("listar_unidades")
    else:
        form = UnidadForm()

    return render(request, "unidades/crear_unidad.html", {
        "form": form
    })

def editar_unidad(request, idUnidad):
    unidad = UnidadServicio.objects.get(pk=idUnidad)

    if request.method == "POST":
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            messages.success(request, "Unidad de servicio actualizada correctamente.")
            return redirect("listar_unidades")
    else:
        form = UnidadForm(instance=unidad)

    return render(request, "unidades/editar_unidad.html", {
        "form": form,
        "unidad": unidad,
    })


def eliminar_unidad(request, idUnidad):
    unidad = UnidadServicio.objects.get(pk=idUnidad)
    unidad.delete()
    messages.success(request, "Unidad de servicio eliminada correctamente.")
    return redirect("listar_unidades")

