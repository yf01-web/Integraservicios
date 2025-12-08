from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_unidades, name='listar_unidades'),
    path('crear/', views.crear_unidad, name='crear_unidad'),
    path('editar/<int:idUnidad>/', views.editar_unidad, name='editar_unidad'),
    path('eliminar/<int:idUnidad>/', views.eliminar_unidad, name='eliminar_unidad'),
]

