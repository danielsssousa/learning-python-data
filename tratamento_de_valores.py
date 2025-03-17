
fim = 0
soma = 0
quantidade = 0

while fim != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma = num + soma
    quantidade += 1
print('Você digitou {} números, A soma de todos os valores digitados a cima são de {}!' .format(quantidade, soma))