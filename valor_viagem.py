dist = float(input('Qual a distancia em Km de sua viagem? '))
print('\033[0;93m-_-\033[m' * 20)

if dist <= 200:
    short = dist * 0.50
    print('Sua viagem foi de {} Km, O valor de sua viagem é de R${:.2f} reais!' .format(dist, short))
else:
    long = dist * 0.45
    print('Sua viagem é {} Km considerada longa, o valor a pagar será de R${:.2f} reias.' .format(dist, long))
print('\033[0;93m-_-\033[m' * 20)
