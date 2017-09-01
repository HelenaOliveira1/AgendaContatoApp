import datetime
from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
import json

listaContato = []
numLinhas= 0

class Contato(Telefone):
    def __init__(self, nome, email, ano, mes, dia, numero, ddd, codigoPais):
        self.criacao = datetime.datetime.now()
        self.pessoa = Pessoa(nome, email, ano, mes, dia)
        super(Contato, self).__init__(numero, ddd, codigoPais)
    
    while True:
        try:
            def AddContatos(self, listaContato, listaelefone):
                nome = str(input("Digite o nome do contato: "))
                email = str(input("Digite Email do contato: "))
                dia = str(input("Digite dia do nascimento: "))
                mes = str(input("Digite mês do nascimento: "))
                ano = str(input("Digite ano do nascimento: "))
                contato = Contato(nome,email,ano,mes,dia,listaTelefone)
                listaContato.append(contato)
                print("Contato Adicionado!")
        
        Except:
            print("Ocorreu um Erro!")
    
    def listarTelefones(self, listaTelefone):
        print("Seus Telefones salvos: ")
        for telefone in listaTelefone:
            print("Telefone: ", telefone)
            
    while True:
        try:
            def ExclusaoContato(self, listaContato):
                nomeExclui = str(input("Qual contato deseja Excluir ? (Digite o nome)"))
                for miniaux in listaContato:
                    if nomeExlui == listaContato[miniaux][nome]:
                        listaContato.pop(miniaux)
                        print("Contato Excluído")
                             
         Except:
            print("Nome não Encontrado!")
            
    while True:
        try:
            def BuscarContato(self)
                print("Buscar Contato: ")
                nomeBusca= str(input("Digite o nome do contato a ser buscado: "))
                for auxzinho in lista contato:
                    if nomeBusca == listaContato[auxzinho][nome]:
                        print("Contato: ", listaContato[auxzinho][nome])
                        print("E-mail: ", listaContato[auxzinho][email])
                        print("Nascimento: ", listaContato[auxzinho][dia],listaContato[auxzinho][mes],listaContato[auxzinho][ano])
                        print("Telefones:", listaContato[auxzinho][telefone])
                        for miniaux in listaTelefone:
                            print(listaTelefone[miniaux]
                
        Except:
            print("Contato não Encontrado!")
