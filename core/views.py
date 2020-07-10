from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .CheckFiles import CheckFiles

def index(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            check = CheckFiles(form.cleaned_data["arquivo1"], form.cleaned_data["arquivo2"]).verifica_tamanho()
            #context = dict(check)
            if type(check) == str:
                return HttpResponse('Os arquivos são iguais!')
            return HttpResponse(check.to_html())
            #return render(request, 'index.html')
            
    else:
        print('Formulário inválido!')
    return render(request, 'index.html', {'form': form})