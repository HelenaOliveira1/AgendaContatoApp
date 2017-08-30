from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
from AgendaContatoApp.Model.Pessoa import Contato
from AgendaContatoApp.Model.Telefone import Agenda

def main():

  op2 = 3
  op1 = int(input("1) Criar Agenda e seu proprietário\n2)Sair"))
  if (op1 == 1):
    Agenda()
  while (op2 != 8):
    op2 = int(input("1) Criar Agenda e seu proprietário\n2) Incluir novo Contato\n3) Listar todos os Contatos\n4) Remover Contato\n5) Buscar Contato\n6) Contar quantidade de contatos\n7) Extrair e Salvar Contato\n8) Sair"))
    if (op2 == 1):
      Agenda()
    elif (op2 == 2):
      IncluirContatos()
    elif (op2 == 3):
      ListarContatos()
    elif (op2 == 4):
      ExcluirContato()
    elif (op2 == 5):
      BuscaDeContato()
    elif (op2 == 6):
      ContarContatos()
    elif (op2 == 7):
      print("JAYSOM")
    elif (op2 == 8):
       print("Programa Encerrado!") 
    else:
       print("Não Há Função!")
      
  else:
    print("Programa Encerrado!")

if __name__ == "__main__":
  main()
