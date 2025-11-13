from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Address
import json

class AddressView(View):

    def get(self, request, *args, **kwargs):
        listaAdress = list(Address.objects.all().values())
        
        return JsonResponse(listaAdress, safe=False)