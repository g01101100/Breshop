import json
from django.test import TestCase, Client
from breshop.models import Address

class AddressTest(TestCase):

    def setUp(self):
        self.client = Client()
        
        self.address01 = {
                "CEP": "09999888",
                "state": "Para",
                "city": "Belem",
                "street": "rua das orquideas",
                "number": 1,
            }
        
        self.address02 = {
                "CEP": "09988888",
                "state": "Bahia",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }
        
        Address.objects.create(**self.address01)


    def test_get_address_url_returns_200(self):
        response = self.client.get('/addresses/')

        self.assertEqual(response.status_code, 200)


    def test_get_returns_created_address(self):
        response = self.client.get('/addresses/')
        addressList = response.json()

        self.assertTrue(len(addressList) > 0)
    
    
    def test_get_address_list_includes_correct_cep(self):
        response = self.client.get('/addresses/')
        addressList = response.json()

        self.assertEqual(addressList[0]["CEP"], '09999888')


    def test_post_addess_url_returns_201(self):
        response = self.client.post('/addresses/', data=json.dumps(self.address02), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    
    def test_post_address_missing_cep(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "state": "Bahia",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_address_whith_spaces_cep(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "        ",
                "state": "Bahia",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_address_invalid_cep_length(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "1234567",
                "state": "Bahia",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_if_post_address_with_special_common_character_in_cep_returns_201(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "12345-678",
                "state": "Bahia",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    
    def test_post_address_missing_state(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_address_whith_spaces_state(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "    ",
                "city": "Salvador",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_address_missing_city(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "Bahia",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_address_whith_spaces_city(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "Bahia",
                "city": "   ",
                "street": "rua das flores",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    
    def test_post_address_missing_street(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "Bahia",
                "city": "salvador",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_address_whith_spaces_street(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "Bahia",
                "city": "salvador",
                "street": "    ",
                "number": 43,
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    
    def test_post_address_missing_number(self):
        response = self.client.post('/addresses/', data=json.dumps({
                "CEP": "09999888",
                "state": "Bahia",
                "city": "salvador",
                "street": "rua das flores",
            }), content_type='application/json')
        self.assertEqual(response.status_code, 400)