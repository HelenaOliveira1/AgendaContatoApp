'''
App.py é o main ou menu, ou seja, a união de todas as funcionalidades para realmente funcionarem
'''

from AgendaContatoApp.Model.Pessoa import Pessoa #importa classe Pessoa
from AgendaContatoApp.Model.Telefone import Telefone #importa classe Telefone
from AgendaContatoApp.Model.Contato import Contato #importa classe Contato
from AgendaContatoApp.Model.Agenda import Agenda #importa classe Agenda
import json #importa o json - leitor de arquivos em formato de dicionário

#sessão de manipulação do Json

def para_dict(obj):                                    #Função recursiva que busca transformar os objetos diretamente em Json
    if hasattr(obj, '__dict__'):                              #inclusive os objetos de super classes e tudo mais
        obj =obj.__dict__
    if isinstance(obj, dict):
        return {k:para_dict(v) for k,v in obj.items()}
    elif isinstance (obj, list) or isinstance (obj, tuple):
        return [para_dict (e) for e in obj]
    else:
        return obj

def PreparandoGeizo():                                     #Definição da função que vai criar e ler o nosso arquivo Json
    try:
        jsonAgenda = open("agenda.json","rw",encoding="utf8")
        agendaJson = json.loads(jsonAgenda.read())
        print(agendaJson)
        json.dump(agendaJson, jsonAgenda, ensure_ascii=False, indent=4)
    except:
        print("Erro no carregamento do arquivo!")

    
def main(Args = []):

    auxiliar = True
    while auxiliar:

        try:
            op2 = 2
            op1 = int(input("1) Criar Agenda e seu proprietário\n2)Sair\n"))

            if (op1 == 1): #Cria a agenda e seu proprietário
                dia = int(input("Digite dia de nascimento: "))
                mes = int(input("Digite mes de nascimento: "))
                ano = int(input("Digite ano de nascimento: "))
                agenda = Agenda(ano, mes, dia)
                print(agenda)
                PreparandoGeizo()    #Ao criar uma agenda, um aquivo Json será criado junto, por mais que não seja utilizado agora
                
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
                        PreparandoGeizo()
                        print("Programa Encerrado!")
                        auxiliar = False
                    else:
                        print("Não Há Função!")

            elif (op1 == 2):
                print("Programa Encerrado!")
                auxiliar = False

            else:
                print("Opção não encontrada!\n")

        except ValueError:
            print("Digite um número inteiro!")

if __name__ == "__main__":
    main()
