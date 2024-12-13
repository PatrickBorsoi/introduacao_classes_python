import pandas as pd

class CsvProcessor:
    #Metodo Construtor(inicialização)
    #Self = todos os parametros que existem na classe
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df
    #recursividade
    ## recebe um vetor de str/ str str[]
    def filtrar_por_coluna(self, colunas, atributos):
        #verificar se as colunas estao populadas
        if len(colunas) != len(atributos):
            raise ValueError("Não tem o mesmo número de colunas e atributos")
        
        if len(colunas) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]

        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por_coluna(colunas[1:], atributos[1:])