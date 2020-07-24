from django.test import TestCase

class InitTest(TestCase):
    """GET / Must returns status code 200"""
    def test_get(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
    
    def test_template(self):
        """Must uses index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')