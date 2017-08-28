import datetime
from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone

class Contato(Telefone):
    def __init__(self, nome, email, ano, mes, dia, numero, ddd, codigoPais):
        self.criacao = datetime.datetime.now()
        self.pessoa = Pessoa(nome, email, ano, mes, dia)
        super(Contato, self).__init__(numero, ddd, codigoPais)

    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print(telefone)