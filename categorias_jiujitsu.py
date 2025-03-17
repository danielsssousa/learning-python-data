from datetime import date

print('''\033[32m

▄▄▄▄· ▄▄▄   ▄▄▄· ·▄▄▄▄•▪  ▄▄▌  ▄▄▌  ▪   ▄▄▄·  ▐ ▄      ▐▄▄▄▪  ▄• ▄▌
▐█ ▀█▪▀▄ █·▐█ ▀█ ▪▀·.█▌██ ██•  ██•  ██ ▐█ ▀█ •█▌▐█      ·████ █▪██▌
▐█▀▀█▄▐▀▀▄ ▄█▀▀█ ▄█▀▀▀•▐█·██▪  ██▪  ▐█·▄█▀▀█ ▐█▐▐▌    ▪▄ ██▐█·█▌▐█▌
██▄▪▐█▐█•█▌▐█ ▪▐▌█▌▪▄█▀▐█▌▐█▌▐▌▐█▌▐▌▐█▌▐█ ▪▐▌██▐█▌    ▐▌▐█▌▐█▌▐█▄█▌
·▀▀▀▀ .▀  ▀ ▀  ▀ ·▀▀▀ •▀▀▀.▀▀▀ .▀▀▀ ▀▀▀ ▀  ▀ ▀▀ █▪     ▀▀▀•▀▀▀ ▀▀▀ 

\033[m''')

print('\033[34m_._\033[m' * 22)
print('''Digite o ano de nascimento do atleta abaixo
para descobrir a categoria em que seu atleta devera competir!''')
print('\033[34m_._\033[m' * 22)



years = int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
years_old = atual - years

if years_old >= 4 and years_old <= 15:
    print('O Atleta competira na \033[31mCategoria Infantil!\033[m')
elif years_old >= 16 and years_old < 18:
    print('O Atleta Competira na \033[31mCategoria Juvenil!\033[m')
elif years_old >= 18 and years_old < 30:
    print('O atleta competira na  \033[31mCategoria Adulto!\033[m')
elif years_old >= 30 and years_old <= 35:
    print('O atleta competira na \033[31mCategoria Master I!\033[m')
elif years_old >= 36 and years_old <= 40:
    print('O Atleta devera competir na \033[31mCategoria Master II\033[m')
else:
    print('Esse já deveria está aposentado! mas pode Competir na Master III mesmo!')

input()