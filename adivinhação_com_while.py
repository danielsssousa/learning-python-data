import random
print(''' \33[33m

 ____             _       _       
/ ___|  ___  _ __| |_ ___(_) ___  
\___ \ / _ \| '__| __/ _ \ |/ _ \ 
 ___) | (_) | |  | ||  __/ | (_) |
|____/ \___/|_|   \__\___|_|\___/ 

\33[m''')
print(''' ===== Sou seu Computador =====
Acabei de pensar em um número de 0 a 10.
Séra que você consegue Adivinhar qual foi?''')
num = int(input('Qual é seu palpite? '))

lista=[1,2,3,4,5,6,7,8,9,10]

correto = random.choice(lista)

tentativas = 0

while correto != num:
    print('\33[31mOpa Errado, tente novamente! \33[m')
    num = int(input('Qual seu palpite? '))
    tentativas += 1

print('''\33[32mParabéns você acertou!\33[m 
Número que pensei foi {}, a sua quantidade de tentativas foi de {}''' .format(num, tentativas))