import AgendaContatoApp.Pessoa

class Agenda():
    def __init__(self, Pessoa):
        self.proprietario = Pessoa

    def ContarContatos(self):
        print("Quantidade de Contatos: ")

    def ListarContatos(self):
        print("Sua lista de Contatos: ")

    def IncluirContatos(self):
        print("Incluir novo contato: ")

    def ExcluirContato(self):
        print("Excluir Contato: ")