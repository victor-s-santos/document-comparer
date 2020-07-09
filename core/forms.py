from django import forms

class UploadFileForm(forms.Form):
    arquivo1 = forms.FileField()
    arquivo2 = forms.FileField()