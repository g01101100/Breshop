from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Brecho, Address
import json

class BrechoView(View):
    
    def get(self, request, *args, **kwargs):
        listaBrecho = list(Brecho.objects.all().values())
        
        return JsonResponse(listaBrecho, safe=False)
