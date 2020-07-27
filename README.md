# CheckFiles Django
> Nesta aplicação, será jogado toda a lógica do notebook CheckFiles, em um servidor Django.

> Como trata-se de um framework python, a ideia de se obter uma melhor visualização do retorno da função, poderá ser obtido através de sua renderização em um template html, utilizando uma função javascript, htmldiff, que trás uma melhor visualização no sentido de identificar onde as diferenças ocorrem no texto.

* __O que foi feito:__
    >- Estruturação do projeto:
    >   - <span style="background-color:green">__Construção dos formulários para receber os arquivos;__</span>
    >   - <span style="background-color:green">__Importar a função e executá-la dentro de uma view do django;__</span>
    >   - <span
    style="background-color:orange">__Página de retorno da função.__

    >- Lógica no Django:
    >   - <span style="background-color:green">__Executar a função usando cada arquivo enviado no input como argumento da funçao;__</span>
    >   - <span style="background-color:green">__Retornar a saída da função dentro de ma view do django;__ </span>

* __Como rodar:__
    > Crie um virtualenv:
    >   - python -m venv .venv
    >   - source .venv/bin/activate
    > Clone do repositório:
    >   - git clone https://github.com/JurisfAI/fAI4-Django
    >   - cd fAI4-Django
    > Instalar as dependências:
    >   - pip install -r requirements.txt
    > Iniciar o servidor:
    >   - python manage.py runserver
    > Rodar os testes:
    >   - python manage.py test