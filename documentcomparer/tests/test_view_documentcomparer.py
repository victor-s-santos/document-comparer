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
        tags_html = (('<form', 1),
                    ('<input', 3),
                    ('type="file"', 1),
                    ('type="submit"', 1)
        )
        for text, count in tags_html:
            with self.subTest():
                self.assertContains(self.response, text, count)

"""Falta entender como criar os testes para a minha função Checkfiles,
e entender como validar o arquivo que está sendo enviado pelo formulário"""
