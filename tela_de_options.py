import time

teste = 0

while teste < 999:

    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))

    soma = num1 + num2
    multi = num1 * num2

    print('''
[1] somar
[2] multiplicar
[3] maior 
[4] novos numeros
[5] sair do programa ''')


    option = int(input('>>> Qual sua opçao? '))
    print('Analisando...')
    time.sleep(1)
    print()


    if option == 1:
        print('\33[32mO resultado da soma dos dois valores sera de {}!\33[m' .format(soma))
    if option == 2:
        print('\33[32mO Resultado da multiplicaçao sera de {}\33[m' .format(multi))
    if option == 3:
        if num1 > num2:
            print('Entre {} e {} O maior numero sera de {}' .format(num1, num2, num1))
        elif num2 > num1:
            print('Entre {} e {} O maior numero sera de {}' .format(num1, num2, num2))
        else:
            print('Os numerais sao iguais!')
    if option == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))

    if option == 5:
        break

    else:
        print('Digite um número valido para prosseguir!')