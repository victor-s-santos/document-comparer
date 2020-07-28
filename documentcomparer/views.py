import pandas as pd
import os
import sys
from django.shortcuts import render
from .forms import UploadFileForm
from .utils.CheckFiles import CheckFiles
#from .validador import FileExtensionValidator


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""BASE_DIR é necessário para criar o caminho dinâmico até o arquivo fixo de comparação"""
arquivo_principal = os.path.join(BASE_DIR, "PrestacaoServico_JurisfAI BASEE.docx")
"""Utilizando a lib os, gerei uma variável que é a string referente ao caminho do arquivo"""

def comparador(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            #check = CheckFiles(form.cleaned_data["arquivo1"], form.cleaned_data["arquivo2"]).verifica_tamanho()
            check = CheckFiles(arquivo_principal, form.cleaned_data["arquivo2"]).verifica_tamanho()
            if type(check) == str:
                return render(request, 'arquivos_iguais.html')
            return render(request, 'tabela.html', {'check': check})
    return render(request, 'formularios.html', {'form': form})