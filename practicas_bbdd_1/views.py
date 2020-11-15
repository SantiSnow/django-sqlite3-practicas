from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    contexto = {
        "NombreApp": "Tienda online de articulos"
    }
    return render(request, 'home.html', contexto)


def articulos(request):
    contexto = {
        "articulos": {
            1: "Primer articulo",
            2: "Segundo articulo",
            3: "Tercer articulo"
        }
    }
    return render(request, 'articulos.html', contexto)
