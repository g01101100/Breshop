from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from breshop.models import Tag
import json

class TagView(View):
    
    def get(self, request, *args, **kwargs):
        listaTags = list(Tag.objects.all().values())
        
        return JsonResponse(listaTags, safe=False)
    
    def post(self, request, *args, **kwargs):
        listaTags = list(Tag.objects.all().values())

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
        
        if {'name': name} in listaTags:
            return JsonResponse({'error': 'this Tag already exist'}, status=400)
        
        if len(name.split()) > 1:
            return JsonResponse({'error': 'the Tag.name must be a single word'}, status=400)
        

        tag = Tag.objects.create(name=name) 
        
        return JsonResponse({
            'name': tag.name
        }, status=201)
        