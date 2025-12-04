from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from breshop.models import Address

import json

@method_decorator(csrf_exempt, name='dispatch')
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
            if type(field) == str:
                if not field.strip():
                    return JsonResponse({'error': 'find some not null field'}, status=400)
            elif type(field) != int:
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
                'CEP': cep,
                'state': state,    
                'city': city,       
                'street': street,    
                'number': number,    
            }, status = 201)    

        response = Address.objects.create(**address)

        return JsonResponse({
            'CEP': response.CEP,
            'state': response.state,    
            'city': response.city,    
            'street': response.street,    
            'number': response.number,    
        }, status = 201)
        
@method_decorator(csrf_exempt, name='dispatch')
class AddressDatailView(View):
    def get(self, request, pk):
        try:
            address = Address.objects.values().get(pk=pk)
        except:
            return JsonResponse({'error': 'Address não encontrada'}, status=404)
        return JsonResponse(address, safe=False)
        
    def delete(self, request, pk):
        try:
            address = Address.objects.get(pk=pk)
            address.delete()
            return JsonResponse({"message": "Address deletada"}, status=200)
        except address.DoesNotExist:
            return JsonResponse({"error": "Address não encontrada"}, status=404)
