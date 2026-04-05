sort_number = 777

print("""

+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+

""")

number = int(input('Digite um numero inteiro: '))

while True:
    if number == 777:
        print()
        print(f'Sortudo, acertou em cheio, o numero de sorte era {sort_number}')
        break
    else:
        print('Ai que burro bro, assim não da! tente novamente!')
        number = int(input('Digite um numero inteiro: '))
