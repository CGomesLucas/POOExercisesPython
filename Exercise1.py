class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        detalhes_lista = {
            "Marca:": self.marca,
            "Modelo:": self.modelo,
            "Ano:": self.ano
        }

        return detalhes_lista

carro1 = Carro("Ford", "Mustang", 2021)
for c, v in carro1.detalhes().items():
    print(c, v)