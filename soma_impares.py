soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma total dos valores será de {}' .format(soma))
