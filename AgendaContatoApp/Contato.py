import datetime
import AgendaContatoApp.Telefone

class Contato():
    def __init__(self):
        self.criacao = datetime.datetime.now ()

    def listarTelefones(self, listaTelefone):
        for telefone in listaTelefone:
            print(telefone)