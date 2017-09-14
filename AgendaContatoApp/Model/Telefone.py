'''
Classe Telefone - definir atributos para telefone pertencente a cada contato
'''

listaTelefone = [] #Define uma lista de telefone

class Telefone():
    def __init__(self):
        self.codigoPais = int(input("Digite o Código do País do telefone: "))
        self.ddd = int(input("Digite o número de ddd do telefone: "))
        self.numero = int(input("Digite o número do telefone: "))
        self.telComplet = ("(" + str(self.codigoPais) + " " + str(self.ddd)+ ") " +str(self.numero))
        listaTelefone.append(self.telComplet) #Adiciona cada telefone criado a uma lista

    def __str__(self): #Alterando método mágico __str__ de Telefone
        return self.telComplet