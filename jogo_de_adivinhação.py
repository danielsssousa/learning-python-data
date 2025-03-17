import random
import emoji
import time

print('-=-' * 20)
print('\33[0;36m Vou Pensar em um número de 0 a 5! Tente adivinhar...\33[m') #Inserir cor se utiliza da expressão \33[0;33;44m
print('-=-' * 20)

num = int(input('Qual número você acha que escolhi? '))

lista = [0,1,2,3,4,5]
escolha = random.choice(lista)

print('Analisando...')
time.sleep(1)

print('O número sorteado foi {}!' .format(escolha))

if num == escolha:
    print(emoji.emojize(':partying_face: Que sortudo ein! Você acertou! Parabéns! :alien:'))
else:
    print(emoji.emojize('Não foi dessa vez campeão :pensive_face:'))