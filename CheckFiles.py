class CheckFiles:
    def __init__(self, f1, f2):
        #refatoração marota
        self.lista1, self.lista2, self.lista_diferenca = [], [], []
        self.document1 = Document(f1).paragraphs
        self.document2 = Document(f2).paragraphs

    def verifica_tamanho(self):
        """Checa se a quantidade de linhas é a mesma para os dois arquivos"""
        for i in range(len(self.document1)):
            self.lista1.append(self.document1[i].text)
        for i in range(len(self.document2)):
            self.lista2.append(self.document2[i].text)
        
        if len(self.lista1) == len(self.lista2):
            return(self.compara_arquivos())
        else:
            return(self.verifica_linhas())

    def compara_arquivos(self):
        """Compara os dois arquivos, linha a linha, dada que a quantidade de linhas é a mesma para os dois"""
        for linha in difflib.unified_diff(self.lista1, self.lista2,fromfile=self.f1, tofile=self.f2, n=1):
            self.lista_diferenca.append(linha)
        lista_zipada = list(zip(self.lista1, self.lista2, self.lista_diferenca))
        if len(lista_zipada) == 0:
            return("Os arquivos são exatamente iguais!")
        df = pd.DataFrame(lista_zipada, columns=['Arquivo1', 'Arquivo2', 'Diferença'])
        df = df.loc[df['Arquivo1'] != df['Arquivo2']]
        return(df)
    
    def verifica_linhas(self):
        """Retorna as linhas que diferem entre si, e as linhas únicas de um dos documentos."""
        if len(self.lista1) > len(self.lista2):
            """Completar a diferença entre as listas com valores vazios"""
            for i in range(len(self.lista2), len(self.lista1)):
                self.lista2.append('Linha vazia')
                """Retornar a função compara_arquivos com o mesmo tamanho para ambas as listas"""
            return(self.compara_arquivos())
        
        if len(self.lista2) > len(self.lista1):
            """Completar a diferença entre as listas com valores vazios"""
            for i in range(len(self.lista1), len(self.lista2)):
                self.lista1.append('Linha vazia')
                """Retornar a função compara_arquivos com o mesmo tamanho para ambas as listas"""
            return(self.compara_arquivos())

