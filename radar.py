
speed = float(input('Qual a velocidade registrada pelo veiculo? '))

if speed <= 80:
     print('\033[0;32m Sua velocidade foi de {} Km/h, boa viagem!\033[m' .format(speed))
else:
     multa = (speed - 80) * 7
     print('\033[0;31mSua velocidade foi de {} Km/h! você foi multado em {:.1f}!\033[m' .format(speed, multa))