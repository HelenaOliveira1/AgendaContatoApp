import datetime
from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone

listaContato = []
contagem = 0
numLinhas= 0

class Contato(Telefone):
    def __init__(self, nome, email, ano, mes, dia, numero, ddd, codigoPais):
        self.criacao = datetime.datetime.now()
        self.pessoa = Pessoa(nome, email, ano, mes, dia)
        super(Contato, self).__init__(numero, ddd, codigoPais)
    
    def AddContatos(self, self.pessoa, self.criacao, self.telefone, contagem, listaContato):
        nome = input()
        email = input()
        nascimento = input()
        nome,email,nascimento)
        telefone = Telefone()
        contato = Contato(nome,email,ano,mes,dia,listaTelefone)
        listaContato.append(contato)
    

    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print("Telefone: ", telefone)
