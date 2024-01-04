from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('principal', views.principal, name='principal'),
    path('regalos', views.regalos, name='regalos'),
    path('viajes', views.viajes, name='viajes'),
    path('detalles', views.detalles, name='detalles'),
    path('fiesta', views.fiesta, name='fiesta'),
    path('mensaje', views.mensaje, name='mensaje'),
    path('recuerdos', views.recuerdos, name='recuerdos'),
    path('contactos', views.contactos, name='contactos'),
    path('empresa', views.empresa, name='empresa'),
    path('servicios', views.servicios, name='servicios'),
    path('productos', views.productos, name='productos'),
    path('globos', views.globos, name='globos'),
    path('celebraciones', views.celebraciones, name='celebraciones'),
    path('videos', views.videos, name='videos'),
]