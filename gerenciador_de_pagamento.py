print('-' * 50)
texto = '\033[34m LOJAS PYTHONCHARM \033[m'
largura = 50
texto_centralizado = texto.center(largura)
print(texto_centralizado)
print('-' * 50)
valor = int(input('Qual valor a ser pago pelo produto? R$ '))
print('''Selecione a forma de pagamento
[1] À Vista dinheiro/cheque.
[2] À Vista no cartão
[3] Em 2x no Cartão
[4] 3x no cartão''')

escolha = int(input('Escolha uma opção de pagamento: '))

if escolha == 1:
    desc = valor - (valor * (10 / 100))
    print()
    print('Sua compra foi aprovada e ficara no valor de R$ {} reais com o desconto de 10%' .format(desc))
elif escolha == 2:
    desc = valor - (valor * (5 / 100))
    print()
    print('Sua compra foi aprovada o valor ficou de R$ {} reais com desconto de 5%' .format(desc))
elif escolha == 3:
    print('Sua compra de R$ {} reais foi aprovada!')
elif escolha == 4:
    desc = (valor + (valor * (20 / 100))) / 3
    print('Sua compra de {} foi aprovada e ficou {} cada parcela com 20% de juros' .format(valor, desc))


input()