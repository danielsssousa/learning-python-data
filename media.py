num1 = int(input('Digite sua primeira nota: '))
num2 = int(input('Digite sua segunda nota: '))

media = (num1 + num2) / 2

if media >= 7:
    print('Voce foi aprovado!')
elif media < 7:
    print('Voce foi reprovado!')