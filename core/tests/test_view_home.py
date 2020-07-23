from django.test import TestCase

class InitTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must returns status_code 200"""
        response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)
    
    def test_template(self):
        """must use index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')
