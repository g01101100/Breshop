import json
from django.test import TestCase, Client
from .models import *

class ProductTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.brecho = Brecho.objects.create(name="brecho01")
        self.tag01 = Tag.objects.create(name="shirt")
        self.tag02 = Tag.objects.create(name="short")
        data01 = {
            "name": "camisa_teste",
            "price": 19.90,
            "brecho": self.brecho,
        }
        data02 = {
            "name": "bermuda_teste",
            "price": 19.90,
            "brecho": self.brecho,
        }
        self.product01 = Product.objects.create(**data01)
        self.product02 = Product.objects.create(**data02)
        self.product01.tags.set([self.tag01, self.tag02])

    
    def test_get_product_url_returns_200(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    
    def test_get_returns_created_product(self):    
        response = self.client.get('/products/')
        productList = response.json()

        self.assertTrue(len(productList) > 0)
        
        
    def test_get_poduct_list_includes_correct_name(self):
        response = self.client.get('/products/')
        productList = response.json()
        
        self.assertEqual(productList[0]["name"], 'camisa_teste')   
    

    def test_product_brecho_relationship_is_corret(self):
        response = self.client.get('/products/')
        productList = response.json()

        brecho_id = productList[0]["brecho_id"]
        brecho = Brecho.objects.get(id=brecho_id)

        self.assertEqual(brecho.name, "brecho01")

    def test_if_product_have_least_one_tag(self):
        tagList = self.product01.tags.all()
        self.assertTrue(tagList)

    def test_product_tag_relationship_is_correct(self):
        tagList = self.product01.tags.all()
        
        self.assertIn(self.tag01, tagList)
        self.assertIn(self.tag02, tagList)



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



class TagTest(TestCase):

    def setUp(self):
        self.client = Client()

        Tag.objects.create(name="Jeans")


    def test_get_tags_url_returns_200(self):
        response = self.client.get('/tags/')

        self.assertEqual(response.status_code, 200)


    def test_get_returns_created_tag(self):
        response = self.client.get('/tags/')
        tagList = response.json()
        
        self.assertTrue(len(tagList) > 0)


    def test_get_tag_list_includes_correct_name(self):
        response = self.client.get('/tags/')
        tagList = response.json()

        self.assertEqual(tagList[0]["name"], 'Jeans')



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
        

        

class AddressTest(TestCase):

    def setUp(self):
        self.client = Client()
        
        address = {
                "CEP": "09999888",
                "state": "Para",
                "city": "Belem",
                "street": "rua das orquideas",
                "number": 1,
            }
        
        Address.objects.create(**address)


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





    
# Create your tests here.
