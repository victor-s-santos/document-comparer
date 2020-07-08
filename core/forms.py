from django import forms

class UploadFileForm1(forms.Form):
    arquivo1 = forms.FileField()

class UploadFileForm2(forms.Form):
    arquivo2 = forms.FileField()