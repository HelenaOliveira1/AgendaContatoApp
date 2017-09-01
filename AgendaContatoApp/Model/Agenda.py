from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
from AgendaContatoApp.Model.Contato import Contato
import json

class Agenda(Contato):
    def __init__(self, nome, email, ano, mes, dia):
        self.proprietario = Pessoa(nome, email, ano, mes, dia)

    def ContarContatos(self, listaContato):
        print("Quantidade de Contatos: ")
        return (len(listaContato)+1)

    def ListarContatos(self, listaContato):
        print("Sua lista de Contatos: ")
        for auxiliadora in listaContato:
            print("Contato: ", listaContato[auxiliadora][nome])
            print("E-mail: ", listaContato[auxiliadora][email])
            print("Nascimento: ", listaContato[auxiliadora][dia],listaContato[auxiliadora][mes],listaContato[auxiliadora][ano])
            print("Telefones:", listaContato[auxiliadora][telefone])
            for miniaux in listaTelefone:
                print(listaTelefone[auxiliadora])

    def IncluirContatos(self,listaContato):
        print("Incluir novo contato: ")
        AddContato()
        

    def ExcluirContato(self):
        print("Excluir Contato: ")
        ExclusaoContato(self, listaContato)

    def BuscaDeContato(self):
        BuscarContato()    
