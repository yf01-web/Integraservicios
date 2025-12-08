from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tipos, name='listar_tipos'),
    path('crear/', views.crear_tipo, name='crear_tipo'),
    path('editar/<int:idTipoRecurso>/', views.editar_tipo, name='editar_tipo'),
    path('eliminar/<int:idTipoRecurso>/', views.eliminar_tipo, name='eliminar_tipo'),
]
