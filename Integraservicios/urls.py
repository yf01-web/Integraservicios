from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("<h1>Bienvenido a IntegraServicios</h1>")

urlpatterns = [

    # Rutas de las apps
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('unidades/', include('unidades.urls')),
    path('tipos/', include('tipos.urls')),
    path('recursos/', include('recursos.urls')),
    path('disponibilidad/', include('disponibilidad.urls')),
    path('reservas/', include('reservas.urls')),
    path('prestamos/', include('prestamos.urls')),
    path('devoluciones/', include('devoluciones.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)