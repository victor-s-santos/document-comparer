import pandas as pd
import os
import sys
from django.shortcuts import render
from .forms import UploadFileForm
from .utils.CheckFiles import CheckFiles





def comparador(request):
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            check = CheckFiles(form.cleaned_data["arquivo1"], form.cleaned_data["arquivo2"]).verifica_tamanho()
            if type(check) == str:
                return render(request, 'arquivos_iguais.html')
            return render(request, 'tabela.html', {'check': check})
    return render(request, 'formularios.html', {'form': form})