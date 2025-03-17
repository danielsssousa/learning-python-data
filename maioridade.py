maior = 0
menor = 0
for c in range(1,5):
    idade = int(input("Digite o ano de nascimento da {}a pessoa: " .format(c)))
    c += 1
    if   2025 - idade >= 18:
        maior += 1
    elif 2025 - idade < 18:
        menor += 1

print('Existem {} maior(es) de idade, e {} menor(es) de idade.' .format(maior, menor))
