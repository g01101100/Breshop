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


    