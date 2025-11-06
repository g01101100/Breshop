from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json


def produtosAPI(request):
    if request.method == 'GET':
        listaProdutos = list(Produto.objects.all().values())
        return JsonResponse(listaProdutos, safe=False)


def cadastrar_Produto(request):
    return render(request, "cadastrar.html")

def alterar_Produto(request):
    return render(request, "alterar.html")

def excluir_Produto(request):
    return render(request, "excluir.html")


# Create your views here.
