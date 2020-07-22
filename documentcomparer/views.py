from django.http import HttpResponse
import pandas as pd
import os
import sys
from django.shortcuts import render
from .forms import UploadFileForm
from .CheckFiles import CheckFiles
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
arquivo_principal = os.path.join(BASE_DIR, "PrestacaoServico_Canon.docx")
def comparador(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            check = CheckFiles(arquivo_principal, form.cleaned_data["arquivo2"]).verifica_tamanho()
            #check.columns = ['arquivo1', 'arquivo2']
            #check.sort_values("Arquivo1", inplace=True)
            if type(check) == str:
                return render(request, 'arquivos_iguais.html')
            #return HttpResponse(check.to_html())
            return render(request, 'tabela.html', {'check': check})
    return render(request, 'formularios.html', {'form': form})