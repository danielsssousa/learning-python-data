
print('Seja bem vindo ao seletor de scripts!')

print('''
    01 > Script de analise de portas na rede aberta.
    02 > Script de verificacao de logs suspeitos.
    03 > Script para criptografia de mensagens em arquivos .txt;
      ''')
      
escolha = 0
   
escolha = int(input('Digite sua escolha:'))

if escolha == 1:
    print('Voce selecionou uma analise de portas de rede abertas, sera realizado o NMap para as demais configuracoes e relatorio.')

else:
    print('Os demais estao em analise!')

    
