import datetime
import AgendaContatoApp.Telefone

listaContato = []

class Contato():
    def __init__(self):
        self.criacao = datetime.datetime.now ()
        listaContato = listaContato.append(Contato)

    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print(telefone)