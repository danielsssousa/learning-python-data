class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

carro = Carro("Ford", 2009, "Amarillo")

print(carro.cor)