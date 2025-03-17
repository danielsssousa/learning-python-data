num = int(input('Digite um número para ver sua tabuada em multiplicação: '))

for c in range(1, 11):
    print( '{} x {} = {}' .format(num,c,  c * num))