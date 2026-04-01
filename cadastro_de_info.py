nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
local = input('Qual cidade você nasceu? ')

print('-' * 45)
print()
print(f'Ola {nome}, vi que você tem {idade} anos, e é da cidade de {local}')



while True:
    resposta = str(input('Para prosseguirmos com o atendimento, você concorda em seguir todas as solicitaçoes requisitadas? S/N '))

    if resposta.lower() == 's':
        print('Tudo bem vamos prosseguir com seu cadastro! Via E-mail, verifique sua caixa!')
        break
        
    elif resposta.lower() == 'n':
        print('Você tera autorização de usuario master caso seja aceito nossos termos e requisições!')
        
        
        
    else:
        print('Digite uma informação valida!')
        
