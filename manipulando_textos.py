#Faz a utilizacao de with.open("Nome do arquivo.txt", formas de abrir) as nomevariavel:
#Existem tres formas de abrir um documento, "w" de writter escrever no arquivo ou cria um arquivo, "r" de read que sera para ler um arquivo e "a" de append, adicionar


#Para leitura de texto!
with open("senhas.txt", "r") as documento:
    senhas = documento.readlines()

    for linhas in senhas:
        if "Espelho" in linhas:
            print(linhas)


#Para escrever um texto!
with open('mensagem.txt', 'w') as arquivo:
    mensagem = arquivo.write('stukas5676')


#Adicionar!