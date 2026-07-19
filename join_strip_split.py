# Estes tres metodos servem para juntar, dividir e limpar textos!

# strip serva para limpar espacos inuteis em uma string, como em um email de usuario no qual ele colocou espacos.

email = str('  meuemail@gmail.com  ')

texto = ' Ola, Pyhton! '

texto_corrijido = email.strip()

print(texto.strip())

print(texto_corrijido)


# split seria o cortador, pois o mesmo divide uma string em listas, quebrando o texto em separadores que o user escolhe ou os espacos se nada for escolhido!

frase = 'Hoje o dia esta maravilhoso!, nao concorda snake?'

print(frase.split(','))

# join, este fica sendo como o colador, o join faz o contrario de split. Ele pega uma lista de strings e junta tudo.

ferramentas = ['maquita', 'parafusadeira', 'chave de fenda', 'alicate']

print(', '.join(ferramentas))
