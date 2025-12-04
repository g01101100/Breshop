from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from breshop.models import Brecho, Address

import json
import re

@method_decorator(csrf_exempt, name='dispatch')
class BrechoView(View):
    
    def get(self, request, *args, **kwargs):
        listaBrecho = list(Brecho.objects.all().values())
        
        return JsonResponse(listaBrecho, safe=False)
    
    def post(self, request, *args, **kwargs):
        listOfBrecho = list(Brecho.objects.all().values())

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)
        
        name = data.get('name')
        email = data.get('email')
        address = data.get('address_id')        
        phone = data.get('phone')
        instagram = data.get('instagram')
        
        listOfNotNullFields = [name, email]
        listOfAllFields = [name, email, address, phone, instagram]


        for field in listOfNotNullFields:
            if type(field) != str:
                return JsonResponse({'error': 'Invalid type field'}, status=400)
            if not field.strip():
                return JsonResponse({'error': 'find some not null field'}, status=400)
        
        for field in listOfAllFields:
            if type(field) == str and re.search(r'[!#$%^&*()+={}\[\]\/\\|;:,\-<>?\'"]', field.strip()):
                return JsonResponse({'error': 'Found invalid caracters in some field'}, status=400)


        

        if not phone.isdigit():
            return JsonResponse({'error': 'Invalid field: phone'}, status=400)
       
        if len(phone) > 12:
            return JsonResponse({'error': 'Too caracters in the field: phone'}, status=400)


        if type(instagram) == str:
            if re.search(r'[ ]', instagram):
                return JsonResponse({'error': 'Found invalid caracters on the field: instagram'}, status=400)
            if len(instagram) > 30:
                return JsonResponse({'error': 'Too caracters on the field: instagram'}, status=400)
            instagram = instagram.strip()
        
        
        brecho = {
            'name': name.strip(),
            'email': email.strip(),
            'address': address,
            'phone': phone.strip(),
            'instagram': instagram,
        }

        if brecho in listOfBrecho:
            return JsonResponse({
                'name': name.strip(),
                'email': email.strip(),
                'address': address,
                'phone': phone.strip(),
                'instagram': instagram.strip(),
            }, status=201)
        
        response = Brecho.objects.create(**brecho)

        return JsonResponse({
            'name': response.name,
            'email': response.email,
            'address': response.address,
            'phone': response.phone,
            'instagram': response.instagram,
        }, status = 201)
    
@method_decorator(csrf_exempt, name='dispatch')
class BrechoDatailView(View):
    def get(self, request, pk):
        try:
            brecho = Brecho.objects.values().get(pk=pk)
        except:
            return JsonResponse({'error': 'brecho não encontrada'}, status=404)
        return JsonResponse(brecho, safe=False)
        
    def delete(self, request, pk):
        try:
            brecho = Brecho.objects.get(pk=pk)
            brecho.delete()
            return JsonResponse({"message": "brecho deletada"}, status=200)
        except brecho.DoesNotExist:
            return JsonResponse({"error": "brecho não encontrada"}, status=404)



