from django.shortcuts import render
from .forms import UploadFileForm1
from .forms import UploadFileForm2

#from funcaoDiffLi import CheckFiles
def printlol():
    print('função aplicada!')
#usar como referência: https://pt.stackoverflow.com/questions/172265/como-eu-crio-2-forms-simultaneamente-django
def index(request):
    if request.method == 'POST':
        form1 = UploadFileForm1(request.POST, request.FILES)
        form2 = UploadFileForm2(request.POST, request.FILES)
        if form1.is_valid():
            #CheckFiles(request.FILES['file'])
            print('Formulário válido!')
    else:
        print('Formulário inválido!')
        form1 = UploadFileForm1()
        form2 = UploadFileForm2()
    return render(request, 'index.html', {'form1': form1, 'form2': form2})
# Create your views here.