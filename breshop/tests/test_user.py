import json
from django.test import TestCase, Client
from breshop.models import User, Address

class UserTest(TestCase):

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
       
        user01 = {
            "name": "Joao",
            "email": "joao@gmail.com"
        }
        user02 = {
            "name": "Carol",
            "email": "carol@gmail.com",
            "address": self.address,
        }
        User.objects.create(**user01)
        User.objects.create(**user02)
        

    def test_get_user_url_returns_200(self):
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, 200)


    def test_get_retuns_created_user(self):
        response = self.client.get('/users/')
        userList = response.json()

        self.assertTrue(len(userList) > 0)


    def test_get_user_list_includes_correct_name_and_email(self):
        response = self.client.get('/users/')
        userList = response.json()

        self.assertEqual(userList[0]["name"], 'Joao')
        self.assertEqual(userList[1]["email"], 'carol@gmail.com')


    def test_user_address_relationship_is_correct(self):
        response = self.client.get('/users/')
        userList = response.json()
        
        address_id = userList[1]["address_id"]
        address = Address.objects.get(id=address_id)

        self.assertEqual(address.city, 'Belem')

    def test_post_user_url_return_201(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "user joao",
            "address": self.address.id,
            "email": "joao@gmail.com",
            }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    

    def test_post_user_missing_name_return_400(self):
        response = Client().post('/users/', data=json.dumps({
            "address": self.address.id,
            "email": "joao@gmail.com",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_user_name_with_spaces_return_400(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "   ",
            "address": self.address.id,
            "email": "joao@gmail.com",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_user_name_with_invalid_caracteres_return_400(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "admin '--",
            "address": self.address.id,
            "email": "joao@gmail.com",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    

    def test_post_user_missing_address_return_201(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "user joao",
            "email": "joao@gmail.com",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        

    def test_post_user_missing_email_return_400(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "user joao",
            "address": self.address.id,
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_user_email_with_spaces_return_400(self):
        response = Client().post('/users/', data=json.dumps({
            "name": "user joao",
            "address": self.address.id,
            "email": "    ",
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)