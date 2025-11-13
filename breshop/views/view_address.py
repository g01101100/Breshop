from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Address
import json

class AddressView(View):

    def get(self, *args, **kwargs):
        listOfAdress = list(Address.objects.all().values())
    
        return JsonResponse(listOfAdress, safe=False)
    
    def post(self, request, *args, **kwargs):
        listOfAddress = list(Address.objects.all().values())

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)
        
        cep = data.get('CEP')
        state = data.get('state')
        city = data.get('city')
        street = data.get('street')
        number = data.get('number')
        
        listOfFields = [cep, state, city, street, number]
        

        for field in listOfFields:
            typeField = type(field)
            if typeField == str:
                field = field.strip()
                if not field:
                    return JsonResponse({'error': 'find some not null field'}, status=400)
            elif typeField != int:
                return JsonResponse({'error': 'find some not null field'}, status=400)
        
        cepCharacters = list(cep)

        if len(cepCharacters) == 9 and cepCharacters[5] == '-':
            cepCharacters.pop(5)
            cep = ''.join(cepCharacters)

        if len(cep.strip('')) != 8:
            return JsonResponse({'error': 'Invalid field: CEP'}, status=400)


        if type(number) != int:
            return JsonResponse({'error': "number invalid type"}, status=400)
        
        state = state.capitalize()
        city = city.capitalize()
        
        address = {
            'CEP': cep,
            'state': state,
            'city': city,
            'street': street,
            'number': number,
        }

        if address in listOfAddress:
            return JsonResponse({
                'CEP': response.CEP,
                'state': response.state,    
                'city': response.city,    
                'street': response.street,    
                'number': response.number,    
            }, status = 201)    

        response = Address.objects.create(**address)

        return JsonResponse({
            'CEP': response.CEP,
            'state': response.state,    
            'city': response.city,    
            'street': response.street,    
            'number': response.number,    
        }, status = 201)
        
