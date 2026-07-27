# A biblioteca pandas é uma das ferramentas mais potentes do ecossistema Python quando o assunto é analisar, filtrar e manipular dados estruturados.

# Nelas existem duas estruturas fundamentais, Series uma unica coluna de dados. e a DataFrame, uma tabela inteira.

import  pandas as pd # A abreviacao pd, ajuda a encurtar o codigo, onde seria usado pandas.DataFrame ou pandas.read_csv() passa a ser pd.DataFrame() e pd.read_csv()


dados = { 
         
         'ip_de_origem': ['192.168.1.10', '10.0.0.5', '192.168.1.10', '172.16.0.2'],
         'portas' : [80, 22, 443, 22],
         'pacotes_enviados' : [150, 12000, 300, 45],
         'status' : ['Permitido', 'Bloqueado', 'Permitido', 'Permitido']   
    
}
# As chaves {} se tornam o titulo da coluna, enquanto a lista [] os dados de cada linha.
# Observe se as listas tem a mesma quantidades de informacoes, caso contrario sera retornado um erro!

# Realizamos a conversao do dicionario em um DataFrame do pandas

df = pd.DataFrame(dados)

print(df)




