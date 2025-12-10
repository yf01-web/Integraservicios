from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recurso, TipoRecurso

@login_required
def catalogo_recursos(request):
    tipos = TipoRecurso.objects.all()
    tipo_filtrado = request.GET.get("tipo", None)

    if tipo_filtrado:
        recursos = Recurso.objects.filter(idTipoRecurso=tipo_filtrado)
    else:
        recursos = Recurso.objects.all()

    return render(request, "recursos/catalogo.html", {
        "recursos": recursos,
        "tipos": tipos,
        "tipo_filtrado": tipo_filtrado
    })

from django.shortcuts import render, get_object_or_404
from .models import Recurso

def detalle_recurso(request, idRecurso):
    recurso = get_object_or_404(Recurso, pk=idRecurso)

    return render(request, "recursos/detalle_recurso.html", {
        "recurso": recurso
    })
