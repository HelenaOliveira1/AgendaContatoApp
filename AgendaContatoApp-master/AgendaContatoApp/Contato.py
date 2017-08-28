import datetime
import AgendaContatoApp.Telefone

listaContato = []

class Contato(Pessoa):
    def __init__(self, nome, nascimento, email):
        pessoa.__init__(self, nome, nascimento, email)
        self.criacao = datetime.datetime.now ()
        listaContato = listaContato.append(Contato)

    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print(telefone)