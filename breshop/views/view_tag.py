from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Tag
import json

class TagListCreateView(View):
    
    def get(self, request, *args, **kwargs):
        listOfTags = list(Tag.objects.all().values())
        
        return JsonResponse(listOfTags, safe=False)
    
    def post(self, request, *args, **kwargs):
        try:            
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'JSON invalid'}, status=400)        
            
        name = data.get('name')
            
        if type(name) != str:
            return JsonResponse({'error': 'this type of name is not valid'}, status=400)
        
        name = name.strip()
        name = name.capitalize()

        if not name:
            return JsonResponse({'error': 'not null field: name'}, status=400)
        
        if len(name) < 3:
            return JsonResponse({'error': 'the Tag.name must be longer than 2 characters'}, status=400)
        

        if Tag.objects.filter(name=name):
            return JsonResponse({'error': 'this Tag already exist'}, status=400)
        
        if len(name.split()) > 1:
            return JsonResponse({'error': 'the Tag.name must be a single word'}, status=400)
        

        tag = Tag.objects.create(name=name) 
        
        
        return JsonResponse({
            'name': tag.name
        }, status=201)
    
class TagDatailView(View):
    def get(self, request, pk):
        try:
            tag = Tag.objects.values().get(pk=pk)
        except:
            return JsonResponse({'error': 'Tag não encontrada'}, status=404)
        return JsonResponse(tag, safe=False)
        