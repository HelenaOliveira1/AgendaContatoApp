from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
from AgendaContatoApp.Model.Contato import Contato

class Agenda(Contato):
    def __init__(self, nome, email, ano, mes, dia):
        self.proprietario = Pessoa(nome, email, ano, mes, dia)

    def ContarContatos(self):
        print("Quantidade de Contatos: ")

    def ListarContatos(self):
        print("Sua lista de Contatos: ")

    def IncluirContatos(self):
        print("Incluir novo contato: ")

    def ExcluirContato(self):
        print("Excluir Contato: ")

    def BuscarContato(self):
        print("Buscar Contato: ")
