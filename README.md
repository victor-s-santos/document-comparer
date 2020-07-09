# CheckFiles Django
> Nesta aplicação, será jogado toda a lógica do notebook CheckFiles, em um servidor Django.

> Como trata-se de um framework python, a idea de se obter uma melhor visualização do retorno da função, poderá ser obtido através de sua renderização em um template html.

* __O que foi feito:__
    >- Estruturação do projeto:
    >   - <div class="text-white bg-green mb-2">__Construção dos formulários para receber os arquivos;__</div>
    >   - <div class="text-white bg-green mb-2">__Importar a função e executá-la dentro de uma view do django;__</div>
    >   - <div class="text-white bg-orange mb-2">__Página de retorno da função.__</div>

    >- Lógica no Django:
    >   - <div class="text-white bg-green mb-2">__Executar a função usando cada arquivo enviado no input como argumento da funçao;__</div>
    >   - <div class="text-white bg-orange mb-2">__Retornar a saída da função dentro de ma view do django;__ </div>


* __Problemas encontrados:__
    >- Lógica no Django:
    >   - Da maneira como estou fazendo, estou gravando os arquivos na memória do servidor, desta forma o arquivo não possue caminho, e este caminho é necessário na aplicação da função.
    >
    >   - Procurando uma maneira de executar a função sem a necessidade de informar o caminho. 