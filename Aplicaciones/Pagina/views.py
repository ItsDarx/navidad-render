from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def principal(request):
    return render(request, 'principal.html')

def regalos(request):
    return render(request, 'regalos.html')

def viajes(request):
    return render(request, 'viajes.html')

def detalles(request):
    return render(request, 'detalles.html')

def fiesta(request):
    return render(request, 'fiesta.html')

def mensaje(request):
    return render(request, 'mensaje.html')

def recuerdos(request):
    return render(request, 'recuerdos.html')

def contactos(request):
    return render(request, 'contactos.html')

def empresa(request):
    return render(request, 'empresa.html')

def servicios(request):
    return render(request, 'servicios.html')

def productos(request):
    return render(request, 'productos.html')

def globos(request):
    return render(request, 'globos.html')

def celebraciones(request):
    return render(request, 'celebraciones.html')

def videos(request):
    return render(request, 'videos.html')