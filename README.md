# CheckFiles Django
> Nesta aplicação, será jogado toda a lógica do notebook CheckFiles, em um servidor Django.

> Como trata-se de um framework python, a idea de se obter uma melhor visualização do retorno da função, poderá ser obtido através de sua renderização em um template html.

* __O que foi feito:__
    >- Estruturação do projeto:
    >   - <span style="background-color:green">__Construção dos formulários para receber os arquivos;__</span>
    >   - <span style="background-color:green">__Importar a função e executá-la dentro de uma view do django;__</span>
    >   - <span
    style="background-color:orange">__Página de retorno da função.__

    >- Lógica no Django:
    >   - <span style="background-color:green">__Executar a função usando cada arquivo enviado no input como argumento da funçao;__</span>
    >   - <span style="background-color:orange">__Retornar a saída da função dentro de ma view do django;__ </span>


* __Problemas encontrados:__
    >- Lógica no Django:
    >   - Da maneira como estou fazendo, estou gravando os arquivos na memória do servidor, desta forma o arquivo não possue caminho, e este caminho é necessário na aplicação da função.
    >
    >   - Procurando uma maneira de executar a função sem a necessidade de informar o caminho. 