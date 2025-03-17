sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalido, digite seu sexo novamente: ')).strip().upper()[0]
print('Seu sexo e {}' .format(sexo))