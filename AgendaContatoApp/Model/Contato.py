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
        nome = input("Digite o nome do contato: ")
        email = input("Digite Email do contato: ")
        dia = input("Digite dia do nascimento: ")
        mes = input("Digite mês do nascimento: ")
        ano = input("Digite ano do nascimento: ")
        contato = Contato(nome,email,ano,mes,dia,listaTelefone)
        listaContato.append(contato)
    

    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print("Telefone: ", telefone)
