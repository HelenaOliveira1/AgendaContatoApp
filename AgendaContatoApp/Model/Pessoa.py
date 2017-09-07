'''
Classe Pessoa - definir atributos de Pessoa
'''

import datetime #Importa a biblioteca de data para usar no nascimento

class Pessoa():
    def __init__(self, ano, mes, dia):
        self.nome = str(input("Digite nome: "))
        self.nascimento = datetime.date(ano, mes, dia)
        self.email = str(input("Digite email: "))

    def __str__(self): #Editando o método mágico __str__ de Pessoa
        return ("  Nome: %s\n  Nascimento: %s\n  Email: %s"%(self.nome, str(self.nascimento), self.email))
