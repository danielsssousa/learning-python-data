class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
#Objeto

meu_carro = Carro('marea', 'amarelo', 1990)

print(meu_carro.cor)

