nome = str(input('Digite seu nome: ')) .strip()
print('Seu nome em Maiusculo é {} '.format(nome.upper()))
print('Seu nome em minusculas é {} '.format(nome.lower()))
print('Seu nome ao todo tem {} letras' .format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras' .format(separa[0], len(separa[0])))



# .strip() Remove os espaços antes e apos o nome.

# - nome.count(' ') Remove os espaços entre os nomes.