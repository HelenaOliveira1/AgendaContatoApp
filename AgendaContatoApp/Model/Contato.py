'''
Classe Contato - definir atributos para um contato
'''

import datetime #Importa a biblioteca de data
from AgendaContatoApp.Model.Pessoa import Pessoa #importa classe Pessoa
from AgendaContatoApp.Model.Telefone import Telefone #importa classe Telefone
import json #importa o json - leitor de arquivos em formato de dicionário

listaContato = [] #Cria uma lista de Contatos Vazia
numLinhas= 0

class Contato(Telefone):
    def __init__(self, ano, mes, dia):
        self.criacao = datetime.date.today()
        self.pessoa = Pessoa(ano, mes, dia)
        self.telContato = Telefone()
        self.contato = (str(self.criacao) + " " + str(self.pessoa) + " " + str(self.telContato))
        listaContato.append(self.contato)

    def __str__(self): #Editando método mágico __str__ de Contato
        return("Data de Criação: " + str(self.criacao) + "\nContato: \n" + str(self.pessoa) + "\nNúmero: " + str(self.telContato))
