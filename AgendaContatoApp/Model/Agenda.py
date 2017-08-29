from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
from AgendaContatoApp.Model.Contato import Contato

class Agenda(Contato):
    def __init__(self, nome, email, ano, mes, dia):
        self.proprietario = Pessoa(nome, email, ano, mes, dia)

    def ContarContatos(self, contagem):
        print("Quantidade de Contatos: ")
        return contagem

    def ListarContatos(self, listaContato):
        print("Sua lista de Contatos: ")
        for contato in listaContato:
            print(contato)

    def IncluirContatos(self):
        print("Incluir novo contato: ")
        Contato.AddContato(self, self.pessoa, self.criacao, self.telefone, contagem, listaContato)
        

    def ExcluirContato(self):
        print("Excluir Contato: ")

    def BuscarContato(self):
        print("Buscar Contato: ")
