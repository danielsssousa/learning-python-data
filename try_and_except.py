
while True:
    try:
        numero = int(input('Digite um numero para realizar sua divisao por 10: '))       
        divisor = 10 / numero
        print(f'O resultado de sua divisao sera de {divisor}')
       
        saida = str(input('Deseja continuar s/n? '))
                
        if saida.lower() not in ['s', 'n']:
            print('Digite uma opcao valida!')
        elif saida.lower() == 's':
            pass
        elif saida.lower() == 'n':
            break
                
    except ZeroDivisionError:
        print('Nao e possivel dividir por 0')
        
    except ValueError:
        print('Digite um caractere valido')
    
    
    