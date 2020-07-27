# CheckFiles Django
> Nesta aplicação, será jogado toda a lógica do notebook CheckFiles, em um servidor Django.

> Como trata-se de um framework python, a ideia de se obter uma melhor visualização do retorno da função, poderá ser obtido através de sua renderização em um template html, utilizando uma função javascript, htmldiff, que trás uma melhor visualização no sentido de identificar onde as diferenças ocorrem no texto.

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
    >   - git clone https://github.com/JurisfAI/fAI4-Django
    >   - cd fAI4-Django
    > Instalar as dependências:
    >   - pip install -r requirements.txt
    > Iniciar o servidor:
    >   - python manage.py runserver
    > Rodar os testes:
    >   - python manage.py test

    * __Testes:__
    > Atualmente os testes se localizam em dois arquivos, um para cada app django:
    > __Core:__
    >   - Os testes da app core possuem a função de verificar o status code da requisição GET(precisa retornar 200);
    >   - E a função de verificar se a aplicação carrega o template correto, no caso index.html;
    >__DocumentComparer:__
    >   - Os testes desta app também verificam o status code e o template, mas também os formulários;
    >   - Verificando a estrutura do html, o csrf, e os campos do formulário, contidos em forms.py;
    >   - Falta implementar os testes de validação do arquivo enviado por input (pois também não existe um validador);
    >   - Falta implementar um teste para o módulo checkfiles, que é o módulo que faz a verificação dos arquivos. 