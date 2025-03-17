salario = float(input('Digite o valor de seu salario atual: R$ '))

if salario <= 1.250:
    novo = salario + (salario * 15 / 100)

else:
    novo = salario + (salario * 10 / 100)

print('O seu salario atual é de R${:.2f} reais, com o reajuste de aumento passa a ser R${:.2f} reais!' .format(salario, novo))