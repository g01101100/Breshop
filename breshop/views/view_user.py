from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from breshop.models import User, Address

import json
import re

@method_decorator(csrf_exempt, name='dispatch')
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
        address_id = data.get('address')        
        
        listOfNotNullFields = [name, email]

        for field in listOfNotNullFields:
            if type(field) != str:
                return JsonResponse({'error': 'Invalid type field'}, status=400)
            if not field.strip():
                return JsonResponse({'error': 'Found Null on not null field'}, status=400)
            

        if type(address_id) != int:
            return JsonResponse({'error': 'wrong address type'}, status=400)

        if not Address.objects.filter(pk=address_id).exists():
            return JsonResponse({'error': 'this address Id not exist'}, status=400)
        
        address = Address.objects.get(pk=address_id)
        
        
        
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
            'address': response.address.id,
        }, status = 201)

@method_decorator(csrf_exempt, name='dispatch')
class UserDatailView(View):
    def get(self, request, pk):
        try:
            user = User.objects.values().get(pk=pk)
        except:
            return JsonResponse({'error': 'user não encontrada'}, status=404)
        return JsonResponse(user, safe=False)
        
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return JsonResponse({"message": "user deletada"}, status=200)
        except user.DoesNotExist:
            return JsonResponse({"error": "user não encontrada"}, status=404)