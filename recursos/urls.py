from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_recursos, name='listar_recursos'),
    path('crear/', views.crear_recurso, name='crear_recurso'),
    path('editar/<int:idRecurso>/', views.editar_recurso, name='editar_recurso'),
    path('eliminar/<int:idRecurso>/', views.eliminar_recurso, name='eliminar_recurso'),
]
