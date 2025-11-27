import json
from django.test import TestCase, Client
from breshop.models import Product, Brecho, Tag

class ProductTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.brecho = Brecho.objects.create(name="brecho01")
        self.tag01 = Tag.objects.create(name="shirt")
        self.tag02 = Tag.objects.create(name="short")
        self.data01 = {
            "name": "camisa_teste",
            "price": 19.90,
            "brecho": self.brecho,
        }
        self.product01 = Product.objects.create(**self.data01)
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


    def test_post_product_url_returns_201(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda teste",
            "price": 19.90,
            "brecho": self.brecho.id,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    

    def test_post_product_missing_name_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "price": 19.90,
            "brecho": self.brecho.id,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_product_name_with_spaces_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "   ",
            "price": 19.90,
            "brecho": self.brecho.id,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)


    def test_post_product_missing_price_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "brecho": self.brecho.id,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_product_with_wrong_price_type_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "price": "19.90",
            "brecho": self.brecho.id,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_product_missing_brecho_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "price": 19.90,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_product_with_wrong_brecho_id_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "price": 19.90,
            "brecho": 0,
            "listOfTags": [self.tag01.id, self.tag02.id],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_product_missing_tag_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "price": 19.90,
            "brecho": self.brecho.id,
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_product_with_wrong_tag_returns_400(self):
        response = self.client.post('/products/', data=json.dumps({
            "name": "bermuda_teste",
            "price": 19.90,
            "brecho": self.brecho.id,
            "listOfTags": ["  shit "],
        }), content_type='application/json')
        self.assertEqual(response.status_code, 400)