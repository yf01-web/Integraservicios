from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tipos, name='listar_tipos'),
    path('crear/', views.crear_tipo, name='crear_tipo'),
]
