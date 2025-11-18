from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import User, Address
import json
import re

class UserView(View):
    
    def get(self, request, *args, **kwargs):
        listaUsers = list(User.objects.all().values())
        return JsonResponse(listaUsers, safe=False)

    def post(self, request, *args, **kwargs):
        listOfUser = list(User.objects.all().values())

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)
        
        name = data.get('name')
        email = data.get('email')
        address = data.get('address_id')        
        
        listOfNotNullFields = [name, email]

        for field in listOfNotNullFields:
            if type(field) != str:
                return JsonResponse({'error': 'Invalid type field'}, status=400)
            if not field.strip():
                return JsonResponse({'error': 'Found Null on not null field'}, status=400)
        
        
        if re.search(r'[!#$%^&*()+={}\[\]\/\\|;:, \-<>?\'"]', email.strip()):
            return JsonResponse({'error': 'Found invalid caracters on field: email'}, status=400)
        
        if re.search(r'[!@#$%^&*()+={}\[\]\/\\|;:,.\-<>?\'"]', name.strip()):
            return JsonResponse({'error': 'Found invalid caracters on field: email'}, status=400)
        
        
        user = {
            'name': name.strip(),
            'email': email.strip(),
            'address': address,
        }

        if user in listOfUser:
            return JsonResponse({
                'name': name.strip(),
                'email': email.strip(),
                'address': address,
            }, status=201)
        
        response = User.objects.create(**user)

        return JsonResponse({
            'name': response.name,
            'email': response.email,
            'address': response.address,
        }, status = 201)
