import pandas as pd #pd qualquer nome
print(pd.__version__)
#df_songs = pd.read_csv('artists-data.csv')
print(df_songs.head()) #Exibe as cinco primeiras linhas

#print(df_songs.to_string()) #Exibe o DataFrame completo como uma string, útil para visualização.

 
#pd.set_option('display.max_rows',3) #Define o número máximo de linhas a ser exibido.

# #Filtragem de Dados: Exemplo de filtragem por colunas e linhas específicas:
#df_filtrado = df_songs[df_songs['Genres'] == Gospel/Religioso]
# print(df_filtrado)

# #Criação de Novas Colunas: adicionar colunas derivadas



# #Leitura de Arquivos Excel e Outros Formatos:
# df_songs_2 = pd.read_excel('lu2.xlsx')
# df_songs_3 = pd.read_json('artists-data.json')
# df_songs_4 = pd.read_html('artists-data.html')
# df_songs_5 = pd.read_sql('artists-data.sql')
