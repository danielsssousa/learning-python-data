soma = 0
contagem = 0

for c in range(1, 7):
    num = int(input('Digite o valor de número {}: ' .format(c)))
    soma = soma + num
    contagem = contagem + 1
print('Você digitou {} números, sua soma total é de {}' .format(contagem, soma))
