listaTelefone = []

class Telefone():
    def __init__(self, numero, ddd, codigoPais, listaTelefone):
        self.numero = numero
        self.ddd = ddd
        self.codigoPais = codigoPais
        listaTelefone = listaTelefone.append(str(codigoPais)+str(ddd)+str(numero))
