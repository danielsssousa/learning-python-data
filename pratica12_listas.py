lista = ['Daniel', 'Denilson', 'Maria', 'Joao']

dicionario = {'Nome': 'Joao', 'Idade': 20, 'Telefone': '989845633654'}

tupla = ("root", "root123") #São imutaveis!

print(lista)
print(dicionario)
print(tupla)

#Manipulação de dicionarios

for key, value in dicionario.items():
    print(f'As chaves são {key}, os valores são {value}!')