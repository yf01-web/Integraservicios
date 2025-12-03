from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('how_work/', views.how_work, name='how_work'),
    path('contact/', views.contact, name='contact'),
    
    # Dashboards según rol
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/empleado/', views.dashboard_empleado, name='dashboard_empleado'),
    path('dashboard/cliente/', views.dashboard_cliente, name='dashboard_cliente'),
]


