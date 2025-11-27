import json
from django.test import TestCase, Client
from breshop.models import Tag

class TagTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.data = {
            "name": "Jeans"
        }

        Tag.objects.create(**self.data)


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

    def test_post_tag_url_returns_201(self):
        response = self.client.post('/tags/', data=json.dumps({'name': 'bag'}), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_tag_what_name_already_exist(self):
        response = self.client.post('/tags/', data=json.dumps({"name": "jeans"}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_tag_missing_name(self):
        response = self.client.post('/tags/', data=json.dumps({'name': ''}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_tag_with_wrong_type(self):
        response = self.client.post('/tags/', data=json.dumps({'name': 3}), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_post_tag_with_only_space_name(self):
        response = self.client.post('/tags/', data=json.dumps({'name': '   '}), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_post_tag_with_multiple_words(self):
        response = self.client.post('/tags/', data=json.dumps({'name': 'camisa preta'}), content_type='application/json')
        self.assertEqual(response.status_code, 400)