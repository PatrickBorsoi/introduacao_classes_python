from interface.classes.csv_class import *
path_arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_csv = CsvProcessor(path_arquivo_csv)

arquivo_csv.carregar_csv()

print(arquivo_csv.filtrar_por_coluna(['estado', 'preço'],['SP', '10,50'] ))

# print(arquivo_csv.df)
# limite_2 = 'RJ'


# path_arquivo_csv_2 = 'exemplo2.csv'
# arquivo_csv2 = CsvProcessor(path_arquivo_csv_2)
# arquivo_csv2.carregar_csv()
# print(arquivo_csv2.filtrar_por_coluna(coluna=filtro, atributo=limite_2))