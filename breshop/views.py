from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def productAPI(request):
    if request.method == 'GET':
        listaProducts = list(Product.objects.all().values())
        return JsonResponse(listaProducts, safe=False)

def userAPI(request):
    if request.method == 'GET':
        listaUsers = list(User.objects.all().values())
        return JsonResponse(listaUsers, safe=False)

def tagAPI(request):
    if request.method == 'GET':
        listaTags = list(Tag.objects.all().values())
        return JsonResponse(listaTags, safe=False)

def brechoAPI(request):
    if request.method == 'GET':
        listaBrecho = list(Brecho.objects.all().values())
        return JsonResponse(listaBrecho, safe=False)

def addressAPI(request):
    if request.method == 'GET':
        listaAdress = list(Address.objects.all().values())
        return JsonResponse(listaAdress, safe=False)


def cadastrar_Produto(request):
    return render(request, "cadastrar.html")

def alterar_Produto(request):
    return render(request, "alterar.html")

def excluir_Produto(request):
    return render(request, "excluir.html")


# Create your views here.
