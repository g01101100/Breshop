import json
from django.test import TestCase, Client
from breshop.models import Brecho, Address

class BrechoTest(TestCase):


    def setUp(self):
        
        self.client = Client()
        address = {
            "CEP": "09999888",
            "state": "Para",
            "city": "Belem",
            "street": "rua das orquideas",
            "number": 1,
        }
        self.address = Address.objects.create(**address)
        
        brecho = {
            "name": "brecho joao",
            "address": self.address,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }

        self.brecho = Brecho.objects.create(**brecho)


    def test_get_brecho_url_returns_200(self):
        response = Client().get('/brechos/')
        
        self.assertEqual(response.status_code, 200)

    
    def test_get_returns_created_brecho(self):
        response = Client().get('/brechos/')
        brechoList = response.json()
        
        self.assertTrue(len(brechoList) > 0)
        

    def test_get_brecho_list_includes_correct_name(self):
        response = Client().get('/brechos/')
        brechoList = response.json()
        
        self.assertEqual(brechoList[0]["name"], 'brecho joao')


    def test_brecho_address_relationship_is_correct(self):
        response = Client().get('/brechos/')
        brechoList = response.json()
        
        address_id = brechoList[0]['address_id']
        address = Address.objects.get(id=address_id)
        
        self.assertEqual(address.city, 'Belem')