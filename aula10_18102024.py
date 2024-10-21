# ###AULA10 - 18/10/2024###
# #
# # Pandas
# #
# import pandas as pd #(pd=alias)
# print(pd.__version__)

# #CRIAÇÃO DE UM DATASET ( BUSCA DE INFORMAÇÕES ( DOWNLOAD)) /DATAFRAME ( CRIA AS INFORMAÇÕES " cria do zero")
# #data chama o dicionário
# data = {'Cargo': ['Analista', 'Gerente', 'Estagiário'], #linhas
#         'Salário': [4500, 9000, 2000]} #colunas
# df = pd.DataFrame(data) #df - qualquer nome
# print(df)


# #CRIAÇÃO DE UMA SÉRIE:

# cargos = pd.Series(['Analista', 'Gerente', 'Estagiário'], index=[1, 2, 3])
# print(cargos)




# import pandas as pd #pd qualquer nome
# print(pd.__version__)

# data_cinema={'Título':['Cidade de Deus','Divertidamente','Uma linda mulher'], 
#                'Ano de Lançamento':[2002,2024,1990],
#                'Gênero':['Drama','Animação','Romance']
# }
# cinema=pd.DataFrame(data_cinema)
# print(cinema)


import pandas as pd #pd qualquer nome
df_musica = pd.read_csv('ClassicDisco.csv')
print(df_musica.head())



