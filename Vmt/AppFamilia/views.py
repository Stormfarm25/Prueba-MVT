from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
# Create your views here.

def Inicio(request):
    plantilla = loader.get_template('FamiliaInicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Padres(request):
    plantilla = loader.get_template('padres.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Hermanos(request):
    plantilla = loader.get_template('hermanos.html')
    documento = plantilla.render()
    return HttpResponse(documento)

def Abuelos(request):
    plantilla = loader.get_template('abuelos.html')
    documento = plantilla.render()
    return HttpResponse(documento)