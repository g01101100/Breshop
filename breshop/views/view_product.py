from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Product, Brecho, Tag
import json

class ProductView(View):
    
    def get(self, request, *args, **kwargs):
        listaProducts = list(Product.objects.all().values())
        return JsonResponse(listaProducts, safe=False)
    
    def post(self, request):
        return JsonResponse()