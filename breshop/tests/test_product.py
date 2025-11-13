import json
from django.test import TestCase, Client
from breshop.models import Product, Brecho, Tag

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
