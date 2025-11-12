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
        listaTags = list(Tag.objects.all().values())

        try:            
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)        
            
        name = data.get('name')
            
        if type(name) != str:
            return JsonResponse({'error': 'this type of name is not valid'}, status=400)
        
        name = name.strip()
        name = name.capitalize()

        if not name:
            return JsonResponse({'error': 'not null field: name'}, status=400)
        
        if len(name) < 3:
            return JsonResponse({'error': 'the Tag.name must be longer than 2 characters'}, status=400)
        
        if {'name': name} in listaTags:
            return JsonResponse({'error': 'this Tag already exist'}, status=400)
        
        if len(name.split()) > 1:
            return JsonResponse({'error': 'the Tag.name must be a single word'}, status=400)
        

        tag = Tag.objects.create(name=name) 
        
        return JsonResponse({
            'name': tag.name
        }, status=201)
        


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
