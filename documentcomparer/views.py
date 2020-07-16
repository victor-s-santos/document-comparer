from django.http import HttpResponse
import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from .CheckFiles import CheckFiles

def comparador(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            check = CheckFiles(form.cleaned_data["arquivo1"], form.cleaned_data["arquivo2"]).verifica_tamanho()
            if type(check) == str:
                return HttpResponse('Os arquivos são iguais!')
            #return HttpResponse(check.to_html())
            return render(request, 'tabela.html', {'check': check})
            
    else:
        print('Formulário inválido!')
    return render(request, 'formularios.html', {'form': form})