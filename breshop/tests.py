import json
from django.test import TestCase, Client
from .models import *

class ProdutoTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.brecho = Brecho.objects.create(name="brecho01")
        self.tag01 = Tag.objects.create(name="shirt")
        self.tag02 = Tag.objects.create(name="short")
        data = {
            "name": "camisa_teste",
            "price": 19.90,
            "brecho": self.brecho,
        }
        produto_teste = Produto.objects.create(**data)
        produto_teste.tags.set([self.tag01, self.tag02])

    
    def test_GET_Produto(self):
        response = self.client.get('/produto/')
        self.assertEqual(response.status_code, 200)
        
        data = response.json()

        self.assertTrue(len(data) > 0)
        self.assertEqual(data[0]["name"], 'camisa_teste')   






    
# Create your tests here.
