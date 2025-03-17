soma = 0
maioridade = 0
nome_mais_velho = ' '
mulher_menos_vinte = 0
for c in range(1, 5):
    print( '====NOME DA {} PESSOA!====' .format(c))
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade atual: '))
    soma = soma + idade
    sexo = str(input('Digite seu sexo M/F: '))
    if c == 1 and sexo in 'Mn':
        maioridade = idade
        nome_mais_velho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_vinte += 1

print('A média de idade do grupo é de {} ' .format(soma / 4))
print('O homem mais velho tem {} anos, e seu nome é {}!' .format(maioridade, nome_mais_velho))
print('No grupo temos {} mulher(es) com menos de 20 anos!' .format(mulher_menos_vinte))