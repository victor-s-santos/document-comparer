from django import forms

class UploadFileForm(forms.Form):
    arquivo1 = forms.FileField(required=False)
    arquivo2 = forms.FileField()