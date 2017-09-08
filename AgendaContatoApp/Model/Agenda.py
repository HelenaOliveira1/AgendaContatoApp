'''
Classe Agenda - define atributos de uma agenda e cria as funções necessárias
'''

from AgendaContatoApp.Model.Pessoa import Pessoa #importa classe Pessoa
from AgendaContatoApp.Model.Telefone import Telefone #importa classe Telefone
from AgendaContatoApp.Model.Contato import Contato #importa classe Contato


class Agenda():
    def __init__(self, ano, mes, dia):
        self.proprietario = Pessoa(ano, mes, dia)

    def ContarContatos(self, listaContato): #Conta o número de contatos que existem na Agenda
        print("Quantidade de Contatos: \n")
        return (len(listaContato))

    def ListarContatos(self, listaContato): #Lista todos os contatos presentes na agenda
        print("Sua lista de Contatos: \n")
        for auxiliadora in listaContato:
            print("Contato: ", listaContato[auxiliadora][self.nome])
            print("E-mail: ", listaContato[auxiliadora][self.email])
            print("Nascimento: ", listaContato[auxiliadora][self.nascimento])
            print("Telefones:", listaContato[auxiliadora][self.telContato])

    def IncluirContatos(self): #Inclui algum novo contato na Agenda
        print("Incluir novo contato: \n")
        Contato()

    def ExcluirContato(self, listaContato): #Exclui algum contato presente na Agenda
        print("Excluir Contato: \n")
        nomeExcluir = str(input("Digite o nome do contato para excluir: "))
        for auxiliadora in listaContato:
            if(nomeExcluir == listaContato[auxiliadora][self.nome]):
                listaContato.pop(auxiliadora) #remove a partir do indice que esta na lista

    def BuscaDeContato(self, listaContato): #Busca algum contato da lista pelo nome
        print("Buscar Contato: \n")
        nomeBuscar = str(input("Digite o nome do contato para buscar: "))
        for auxiliadora in listaContato:
            if (nomeBuscar == listaContato[auxiliadora][self.nome]):
                print(listaContato[auxiliadora]) #Exibe o contato

    def __str__(self):
        return ("Proprietário da Agenda: \n" + str(self.proprietario))

