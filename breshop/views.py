from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import *
import json

class ProductView(View):
    
    def get(self, request, *args, **kwargs):
        listaProducts = list(Product.objects.all().values())
        return JsonResponse(listaProducts, safe=False)
    
    def post(self, request):
        return JsonResponse()

class UserView(View):
    
    def get(self, request, *args, **kwargs):
        listaUsers = list(User.objects.all().values())
        return JsonResponse(listaUsers, safe=False)


class TagView(View):
    
    def get(self, request, *args, **kwargs):
        listaTags = list(Tag.objects.all().values())
        
        return JsonResponse(listaTags, safe=False)
    
    def post(self, request, *args, **kwargs):

        try:            
            data = json.loads(request.body)
            name = data['name']
            
            if not name:
                return JsonResponse({'error': 'not null field: name'}, status=400)
            
            tag = Tag.objects.create(name=name) 
            
            return JsonResponse({
                'name': tag.name
            }, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)        

class BrechoView(View):
    
    def get(self, request, *args, **kwargs):
        listaBrecho = list(Brecho.objects.all().values())
        
        return JsonResponse(listaBrecho, safe=False)


class AddressView(View):

    def get(self, request, *args, **kwargs):
        listaAdress = list(Address.objects.all().values())
        
        return JsonResponse(listaAdress, safe=False)


def cadastrar_Produto(request):
    return render(request, "cadastrar.html")

def alterar_Produto(request):
    return render(request, "alterar.html")

def excluir_Produto(request):
    return render(request, "excluir.html")


# Create your views here.
