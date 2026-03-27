saldo = 0
valor = 0
total  = 0

soldo = float(input('Digite seu soldo: '))

while True:
    finalizar = input('Digite a descrição da despesa ou SAIR para encerrar: ')

    if finalizar.lower() == 'sair':
        print('Finalizando...')
        print('_' * 30)
        print(f"Seu total de divida é de R$ {total}")

        break

    valor = float(input('Digite o  valor da divida: '))

    total += valor  ## clean code de total = valor + total 
    

    


