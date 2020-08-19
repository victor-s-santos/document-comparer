# Comparador de Documentos(.docx) com Django
> Nesta aplicação, será jogado toda a lógica de uma aplicação python que lê e compara dois arquivos tipo .docx, sendo o servidor do django usado para que isto possa se tornar uma aplicação web.

> Como trata-se de um framework python, a ideia de se obter uma melhor visualização do retorno da função, poderá ser obtido através de sua renderização em um template html, utilizando uma função javascript, htmldiff, que trás uma melhor visualização no sentido de identificar onde as diferenças ocorrem no texto.

>Outro ponto a se destacar, é como utilizando o django, o projeto deixou de ser um script python e passou a ser uma aplicação web, tornando-se desta forma muito mais flexível.

* __O que foi feito:__
    >- Estruturação do projeto:
    >   -__Construção dos formulários para receber os arquivos;__
    >   -__Importar a função e executá-la dentro de uma view do django;__
    >   -__Página de retorno da função.__

    >- Lógica no Django:
    >   -__Executar a função usando cada arquivo enviado no input como argumento da funçao;__
    >   -__Retornar a saída da função dentro de ma view do django;__

* __Como rodar:__
    > Crie um virtualenv:
    >   - python -m venv .venv
    >   - source .venv/bin/activate
    > Clone do repositório:
    >   - git clone https://github.com/victor-s-santos/document-comparer.git
    >   - cd document-comparer
    > Instalar as dependências:
    >   - pip install -r requirements.txt
    > Iniciar o servidor:
    >   - python manage.py runserver