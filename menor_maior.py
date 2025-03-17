a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

menor = a
maior = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor será {}!' .format(menor))
print('O maior valor é de {}' .format(maior))