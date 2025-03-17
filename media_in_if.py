import emoji

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('''''')
if media < 5.0:
    print(emoji.emojize('''REPROVADO
Sua média foi de {:.1f} :sad_but_relieved_face:''') .format(media))

elif media > 5.0 and media < 6.9:
    print(emoji.emojize('''RECUPERAÇÃO!
Sua media foi de {:.1f} :books:''') .format(media))

elif media >= 7.0:
    print(emoji.emojize('''APROVADO!
Sua media foi de {:.1f} :partying_face:''') .format(media))