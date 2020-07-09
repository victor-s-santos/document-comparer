import io
from django.shortcuts import render
from .forms import UploadFileForm
from .CheckFiles import CheckFiles
# from .forms import UploadFileForm2

# from funcaoDiffLi import CheckFiles
#usar funções dentro da view https://stackoverflow.com/questions/36124022/how-to-create-a-function-is-views-py-so-that-all-the-functions-inside-the-views
def index(request):
    #c = CheckFiles('./arquivos_iguais/file1.docx', 'arquivos_iguais/file1.docx')
    form = UploadFileForm(request.POST, request.FILES)
    if request.method == 'POST':
        #form1 = UploadFileForm1(request.POST, request.FILES)
        if form.is_valid():
            check = CheckFiles(form.cleaned_data["arquivo1"], form.cleaned_data["arquivo2"])
            print('Formulário válido!')
    else:
        #c.verifica_tamanho()
        print('Formulário inválido!')
        #form1 = UploadFileForm1()
    return render(request, 'index.html', {'form': form})