import time
import random

print('BEM VINDO AO GAME JO-KEN-PO!')

print('''Escolha uma opção!
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')

lista = [1,2,3]
maquina = random.choice(lista)

escolha_jogador = int(input('Digite sua o número de sua opção: '))

print('JO!')
time.sleep(1)
print('KEN!')
time.sleep(1)
print('PO!')

if escolha_jogador == maquina:
    print('O game empatou! Tente novamente!')



elif escolha_jogador == 1 and maquina == 2:
    print('Você perdeu você escolheu [{}] PEDRA, enquanto seu adversario [{}] PAPEL!' .format(escolha_jogador, maquina))
elif escolha_jogador == 1 and maquina == 3:
    print('Você GANHOU! sua escolha foi {} PEDRA enquanto do seu oponente {} TESOURA!' .format(escolha_jogador, maquina))
elif escolha_jogador == 2 and maquina == 1:
    print('Você GANHOU! sua escolha de {} PAPEL vence a {} PEDRA' .format(escolha_jogador, maquina))
elif escolha_jogador == 2 and maquina == 3:
    print('Você PERDEU! Sua escolha de {} PAPEL, perde para {} TESOURA!' .format(escolha_jogador, maquina))
elif escolha_jogador == 3 and maquina == 1:
    print('Você PERDEU! {} TESOURA, perde para {} PEDRA!' .format(escolha_jogador, maquina))
elif escolha_jogador == 3 and maquina == 2:
    print('Você GANHOU! {} TESOURA ganha de {} PAPEL!' .format(escolha_jogador, maquina))

input()




