key = 2345

user_key = int(input('Digite a senha de 04 (Quatro) Digitos: '))
if user_key == key:
    print('Acesso autorizado!')


while user_key != key:
    user_key = int(input('''Senha incorreta! 
Tente novamente: '''))
    if user_key == key:
     print('Acesso autorizado!')
     break







