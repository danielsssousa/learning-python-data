num = int(input('Digite um número: '))
soma = num % 3
if soma == 0:
    print('Você digitou {}, seu número é par!' .format(num))
else:
    print('Você digitou {}, seu número é impar!' .format(num))