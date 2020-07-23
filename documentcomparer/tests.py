from django.test import TestCase

class DocumentComparerTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/documentcomparer/')

    def test_get(self):
        """GET /documentcomparer/ must returns status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must uses /documentcomparer/formularios.html"""
        self.assertTemplateUsed(self.response, 'formularios.html')

    def test_htmltags(self):
        """Verify html tags"""
        self.assertContains(self.response, '<form', 1)
        #gambiarra aqui, por conta disso defino como 3 inputs
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, 'type="file"', 1)
        self.assertContains(self.response, 'type="submit"', 1)

"""Falta entender como criar os testes para a minha função Checkfiles"""