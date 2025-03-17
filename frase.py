frase = str(input('Digite sua frase: ')).upper().strip()
print('Sua frase tem {} letras A!' .format(frase.count('A')))
print('A letra A aparece a primeira vez na {}a posição!' .format(frase.find('A')+1))
print('Sua ultima posiçao é a {}a!' .format(frase.rfind('A')+1))