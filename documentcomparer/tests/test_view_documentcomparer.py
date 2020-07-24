from django.test import TestCase
from .forms import UploadFileForm

class ComparadorTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/canon/')
    
    def test_get(self):
        """GET /canon/ Must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use template canon/formularios.html"""
        self.assertTemplateUsed(self.response, 'formularios.html')

    def test_html_structure(self):
        """Define the html structure"""
        tags_html = (('<form', 1),
                    ('<input', 3),
                    ('type="file"', 1),
                    ('type="submit"', 1)
        )
        for text, count in tags_html:
            with self.subTest():
                self.assertContains(self.response, text, count)
        #self.assertContains(self.response, '<form', 1)
        #self.assertContains(self.response, '<input', 3)
        #self.assertContains(self.response, 'type="file"', 1)
        #self.assertContains(self.response, 'type="submit"', 1)

    def test_csfr(self):
        """Html page must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have UploadFileForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, UploadFileForm)

    def test_form_has_fields(self):
        """Form must have 2 fields"""
        form = self.response.context['form']
        self.assertSequenceEqual(['arquivo1', 'arquivo2'], list(form.fields))