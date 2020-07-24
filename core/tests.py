from django.test import TestCase

class InitTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / Must returns status code 200"""
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """Must uses index.html"""
        self.assertTemplateUsed(self.response, 'index.html')