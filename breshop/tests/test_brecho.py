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
        
        brecho01 = {
            "name": "brecho joao",
            "address": self.address,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }
        self.brecho02 = {
            "name": "brecho joao",
            "address": self.address,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }

        self.brecho = Brecho.objects.create(**brecho01)


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

    
    def test_post_brecho_url_return_201(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
            }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    

    def test_post_brecho_missing_name_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_brecho_name_with_spaces_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "   ",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    

    def test_post_brecho_missing_address_return_201(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        

    def test_post_brecho_missing_email_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "phone": "82988888888",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_brecho_email_with_spaces_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "    ",
            "phone": "82988888888",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    

    def test_post_brecho_missing_phone_return_201(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82912345678",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_brecho_phone_with_spaces_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "   ",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_brecho_phone_with_letters_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82912345ab8",
            "instagram": "joao123",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    

    def test_post_brecho_missing_instagram_return_201(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_post_brecho_instagram_with_spaces_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "  ",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_brecho_instagram_with_more_than_30_caracteres_return_400(self):
        response = Client().post('/brechos/', data=json.dumps({
            "name": "brecho joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            "phone": "82988888888",
            "instagram": "abcdefghijklmnopqrstuvwabcdefgh",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    