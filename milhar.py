num = int(input('Digite um número: '))
und = num // 1 % 10
dez = num // 10 % 10
cent = num // 100 % 10
mil = num // 1000 % 10
print(' Analisando o numero {}' .format(num))
print('Unidade: {}' .format(und))
print('Dezena: {}' .format(dez))
print('Centena: {}' .format(cent))
print('Milhar: {} '.format(mil))