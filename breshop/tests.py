import json
from django.test import TestCase, Client
from .models import *

class ProdutoTest(TestCase):

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

class UserTest(TestCase):

    def setUp(self):
        self.client = Client()
       
        adress = {
            "CEP": "09999888",
            "state": "Para",
            "city": "Belem",
            "street": "rua das orquideas",
            "number": 1,
        }
        self.adress = Adress.objects.create(**adress)
       
        user01 = {
            "name": "Joao",
            "email": "joao@gmail.com"
        }
        user02 = {
            "name": "Carol",
            "email": "carol@gmail.com",
            "adress": self.adress,
        }
        User.objects.create(**user01)
        User.objects.create(**user02)
        

    def test_GET_User(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)

        listUser = response.json()

        self.assertTrue(len(listUser) == 2)

        self.assertEqual(listUser[0]["name"], 'Joao')
        self.assertEqual(listUser[1]["email"], 'carol@gmail.com')
        
        adress_id = listUser[1]["adress"]
        adress = Adress.objects.get(id=adress_id)
        self.assertEqual(adress.city, 'Belem')





    
# Create your tests here.
