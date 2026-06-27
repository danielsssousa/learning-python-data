class Cadastro_Netflix:
    def __init__(self,nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano invalido')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano Invalido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Faca um upgrade para ver este filme')
        else:
            print('Plano Invalido')


cliente = Cadastro_Netflix('Daniel','daniel@gmail.com', 'Basic')
print(cliente.plano)
cliente.ver_filme('Spider men 2', 'Premium')

#Com button Upgrade

cliente.mudar_plano('Premium')
print(cliente.plano)
cliente.ver_filme('Spider men 2', 'Premium')


