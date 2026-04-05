numer1 = int(input('Digite seu priveiro valor: '))
numer2 = int(input('Digite seu segundo valor: '))
numer3 = int(input('Digite seu terceiro valor: '))

maior = 0

if numer1 >= numer2 and numer1 >= numer3: #Sintaxe de comparação correta apos o 'and'
    maior = numer1
elif numer2 >= numer1 and numer2 >= numer3: #Utilizar o >= é uso de uma boa pratica no codigo.
    maior = numer2
else:
    maior = numer3

print(f'O maior número é de {maior}')

print()
print('='*45)
print()

#Utilizando a função MAX

valor1 = float(input('Digite o primeiro valor:'))
valor2= float(input('Digite o segundo valor'))
valor3= float(input('Digite o terceiro valor:'))

maior = max(valor1, valor2, valor3) #Função nativa 'max'

print(f'Seu maior valor é de {maior}')