from django.http import JsonResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from breshop.models import Product, Brecho, Tag
import json

@method_decorator(csrf_exempt, name='dispatch')
class ProductView(View):
    
    def get(self, request, *args, **kwargs):
        listaProducts = list(Product.objects.all().values())
        return JsonResponse(listaProducts, safe=False)
    
    def post(self, request, *args, **kwargs):
        listOfProduct = list(Product.objects.all().values())

        try:            
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)        
            
        name = data.get('name')
        price = data.get('price')
        brecho_id = data.get('brecho')
        tagsIdList = data.get('listOfTags', [])
        listOfFields = [name, price, brecho_id, tagsIdList]  
        
        for field in listOfFields:
            if type(field) == str:
                field = field.strip()
            if not field:
                return JsonResponse({'error': 'Not null field'}, status=400)

        
        for tagId in tagsIdList:
            if type(tagId) != int:
                return JsonResponse({'error': 'wrong tag type'}, status=400)
        
        tags = Tag.objects.filter(pk__in=tagsIdList)


        if type(brecho_id) != int:
            return JsonResponse({'error': 'wrong Brecho type'}, status=400)

        if not Brecho.objects.filter(pk=brecho_id).exists():
            return JsonResponse({'error': 'this brecho Id not exist'}, status=400)
            
        brecho = Brecho.objects.get(pk=brecho_id)

        if not isinstance(price, (int, float)):
            return JsonResponse({'error': 'wrong price type'}, status=400)
        
        price = float(price)


        if(type(tagsIdList) != list):
            return JsonResponse({'error': 'Wrong type of listOfTags'}, status=400)
        
        if len(tagsIdList) != len(tags):
            return JsonResponse({'error': 'one or many tags not exist'}, status=400)
        

        product = {
            'name': name.strip(),
            'price': price,
            'brecho': brecho,
        } 

        response = Product.objects.create(**product)

        response.tags.set(tags)

        return JsonResponse({
            'name': response.name,
            'price': response.price,
            'brecho': response.brecho.id,
            'Tags_list': list(response.tags.values_list('id', flat=True))
        }, status=201)   
    
@method_decorator(csrf_exempt, name='dispatch')
class ProductDatailView(View):
    def get(self, request, pk):
        try:
            product = Product.objects.values().get(pk=pk)
        except:
            return JsonResponse({'error': 'product não encontrada'}, status=404)
        return JsonResponse(product, safe=False)
        
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return JsonResponse({"message": "product deletada"}, status=200)
        except product.DoesNotExist:
            return JsonResponse({"error": "product não encontrada"}, status=404)
