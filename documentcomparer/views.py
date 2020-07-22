from django.http import HttpResponse
import pandas as pd
import os
import sys
from django.shortcuts import render
from .forms import UploadFileForm
from .CheckFiles import CheckFiles

def comparador(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            check = CheckFiles(os.path.join(sys.path[0], "PrestacaoServico_Canon.docx"), form.cleaned_data["arquivo2"]).verifica_tamanho()
            check.columns = ['arquivo1', 'arquivo2']
            #check.sort_values("Arquivo1", inplace=True)
            if type(check) == str:
                return render(request, 'arquivos_iguais.html')
            #return HttpResponse(check.to_html())
            return render(request, 'tabela.html', {'check': check})
    return render(request, 'formularios.html', {'form': form})