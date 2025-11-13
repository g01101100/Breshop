from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import User, Address
import json

class UserView(View):
    
    def get(self, request, *args, **kwargs):
        listaUsers = list(User.objects.all().values())
        return JsonResponse(listaUsers, safe=False)
