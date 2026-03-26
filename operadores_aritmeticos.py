
try:
    a = int(input("Digite um valor: "))
    b = int(input('Digite outro valor: '))

    soma = a+b 

    print(f'O resultado de sua soma sera de {soma}')

except ValueError:
    print('Digite um numero valido')