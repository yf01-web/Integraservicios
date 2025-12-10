from django.urls import path
from . import views
from . import views_catalogo

urlpatterns = [
    # CRUD admin
    path('', views.listar_recursos, name='listar_recursos'),
    path('crear/', views.crear_recurso, name='crear_recurso'),
    path('editar/<int:idRecurso>/', views.editar_recurso, name='editar_recurso'),
    path('eliminar/<int:idRecurso>/', views.eliminar_recurso, name='eliminar_recurso'),

    # Catálogo público (cliente y empleado)
    path('catalogo/', views_catalogo.catalogo_recursos, name='catalogo_recursos'),
    path('catalogo/detalle/<int:idRecurso>/', views_catalogo.detalle_recurso, name='detalle_recurso'),
]
