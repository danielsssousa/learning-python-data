import random

nome1 = str(input('Digite o participante Nr 01: '))
nome2 = str(input('Digite o participante Nr 02: '))
nome3 = str(input('Digite o participante Nr 03: '))
nome4 = str(input('Digite o participante Nr 04: '))

lista = [nome1, nome2, nome3, nome4]

sorteado = random.choice(lista)

print('\033[0;92m O Sorteado foi o participante {} \033[m' .format(sorteado))