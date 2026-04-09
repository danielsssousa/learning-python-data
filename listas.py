numeros = [23, 54, 102, 45]

print(f'Lista atual {numeros}')

numeros[3] = 111

print(f'\nLista anterior {numeros}')

numeros[1] = 100

print(f'Tabela nova {numeros}')

print(f'\nList length', len(numeros)) #Le o comprimento da lista


del numeros[1]
print('\nlist lengh', len(numeros))
print(numeros)