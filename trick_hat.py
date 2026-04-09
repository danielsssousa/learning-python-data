hat = [1,2,3,4,5]

removendo = int(input('Escolha um numero inteiro: '))

del hat[-1]

hat[2] = removendo
print(len(hat))
print(hat)