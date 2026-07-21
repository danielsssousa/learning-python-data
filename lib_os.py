# A biblioteca OS e um dos modulos nativos do python, a mesma permite que o codigo converse diretamente com o sistema operacional.

import os

# Retorna o diretório atual onde seu script está rodando
print('Yo estoy in ', os.getcwd())

# Lista todas as pastas no caminha atual

os.rmdir('scripts')

if not os.path.exists('scripts'):
    os.mkdir('scripts')
    print('Pasta criada com sucesso!')

else:
    print('Ja existe um pasta com este nome')
#os.makedirs('logs/hash') # Cria um aninhamento de pasta e subpastas.
#os.rename('scripts', 'code') # renomeia pastas ou arquivos.
#os.remove('teste.txt') # apaga um arquivo
#os.rmdir('code') # Apaga uma pasta vazia

print('Diretorios disponiveis', os.listdir())