valor_casa = float(input('Qual o valor da casa pretendida? '))
salario = float(input('Qual seu salario? '))
tempo = int(input('Em qunatos anos voce pretende pagar? '))
prestacao = valor_casa / (tempo * 12)
minimo = salario * 30/100
if prestacao <= minimo:
    print('EMprestimo AUTORIZADO!')
else:
    print('Empretimo NEGADO!')