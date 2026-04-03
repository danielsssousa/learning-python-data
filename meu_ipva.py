#Sintaxe de um parametro: def nome_da_funcao(parametros): codigo return valor

def soma(a, b):
    resultado = a + b

    return resultado

def multi(a, b):
    resultado = a * b
    return resultado


print(f'Resultado {soma(20, 30)}') #Deve ser inserida a funcao nao a variavel
print(f'Rsultado da multiplicacao {multi(20, 5)}')


def ola(nome):
    saudacao = f'seja bien venindo {nome}'
    return saudacao

print(ola('Matheus'))

