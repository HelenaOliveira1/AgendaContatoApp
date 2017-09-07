'''
App.py é o main ou menu, ou seja, a união de todas as funcionalidades para realmente funcionarem
'''

from AgendaContatoApp.Model.Pessoa import Pessoa #importa classe Pessoa
from AgendaContatoApp.Model.Telefone import Telefone #importa classe Telefone
from AgendaContatoApp.Model.Contato import Contato #importa classe Contato
from AgendaContatoApp.Model.Agenda import Agenda #importa classe Agenda

def main():
    while True:

        try:
            op2 = 2
            op1 = int(input("1) Criar Agenda e seu proprietário\n2)Sair\n"))

            if (op1 == 1): #Cria a agenda e seu proprietário
                dia = int(input("Digite dia de nascimento: "))
                mes = int(input("Digite mes de nascimento: "))
                ano = int(input("Digite ano de nascimento: "))
                agenda = Agenda(ano, mes, dia)
                print(agenda)

                while (op2 != 0): #Exibe o menu e pede uma das opções ao usuário

                    op2 = int(input("1) Incluir novo Contato\n2) Listar todos os Contatos\n3) Remover Contato\n4) Buscar Contato\n5) Contar quantidade de contatos\n0) Sair\n"))

                    if (op2 == 1):
                        Agenda.IncluirContatos()
                    elif (op2 == 2):
                        Agenda.ListarContatos()
                    elif (op2 == 3):
                        Agenda.ExcluirContato()
                    elif (op2 == 4):
                        Agenda.BuscaDeContato()
                    elif (op2 == 5):
                        Agenda.ContarContatos(Contato.listaContato)
                    elif (op2 == 0):
                        print("Programa Encerrado!")
                    else:
                        print("Não Há Função!")

            else:
                print("Programa Encerrado!")

        except ValueError:
            print("Digite um número inteiro!")

if __name__ == "__main__":
    main()
