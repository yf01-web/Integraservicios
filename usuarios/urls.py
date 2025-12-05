from django.urls import path
from . import views

urlpatterns = [

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboards (Homes según rol)
    path('dashboard/', views.dashboard_redirigir, name='dashboard'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/empleado/', views.dashboard_empleado, name='dashboard_empleado'),
    path('dashboard/cliente/', views.dashboard_cliente, name='dashboard_cliente'),
]
