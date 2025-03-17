print(''' ("`-''-/").___..--''"`-._ 
 `6_ 6  )   `-.  (     ).`-.__.`) 
 (_Y_.)'  ._   )  `._ `. ``-..-' 
   _..`--'_..-_/  /--'_.'
  ((((.-''  ((((.'  (((.-' ''')

from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}!' .format(nasc, idade, atual))

if idade == 18:
    print('Você tem de se alistar imediatamente!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para você se alistar!' .format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos atras!!!' .format(saldo))
