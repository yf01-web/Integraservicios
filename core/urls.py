from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('how_work/', views.how_work, name='how_work'),
    path('contact/', views.contact, name='contact'),
    
]


