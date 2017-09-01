from AgendaContatoApp.Model.Pessoa import Pessoa
from AgendaContatoApp.Model.Telefone import Telefone
from AgendaContatoApp.Model.Pessoa import Contato
from AgendaContatoApp.Model.Telefone import Agenda

def main():
  
    try:
      if 
  op2 = 3
  op1 = int(input("1) Criar Agenda e seu proprietário\n2)Sair"))
  if (op1 == 1):
    Agenda = Agenda (nome, email, ano, mes, dia)
  while (op2 != 7):
    op2 = int(input("1) Criar Agenda e seu proprietário\n2) Incluir novo Contato\n3) Listar todos os Contatos\n4) Remover Contato\n5) Buscar Contato\n6) Contar quantidade de contatos\n7) Sair"))
    if (op2 == 1):
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
       print("Programa Encerrado!") 
    else:
       print("Não Há Função!")
      
  else:
    print("Programa Encerrado!")
    
     def para_dict(obj)                                                      #TRANSFORMAR AS PORRA TUDO EM DICIONÁRIO
        if hasattr(obj, '__dict__'):                                        # ATÉ OS CARAI DE HERANÇA
            obj =obj.__dict__
        if isinstance(obj, dict):
            return {k:para_dict(v) for k,v in obj.items()  }
        elif isinstance (obj, list) or isinstance (obj, tuple):
            return [para_dict (e) for e in obj]
        else:
            return obj
        
    
           
    def PreparandoGeizo(self): 
            try:
                jsonAgenda = open("agenda.json","r")
                self.agendaJson = json.load(jsonAgenda)
                print(self.agendaJson)
            except:
                print("erro no carregamento do arquivo")


    def salvandoGeizo(self):       
            try:
                jsonAgenda = open("agenda.json","w")
                jsonStrinAgenda = self.agendaJson
                jsonStrinAgenda = json.dumps(para_dict(Agenda))
                jsonAgenda.write(jsonStrinAgenda)
            except:
    
    

if __name__ == "__main__":
  main()
