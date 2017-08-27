import datetime

class Pessoa():
    def __init__(self, nome, email, ano, mes, dia):
        self.nome = nome
        self.nascimento = datetime.date(ano, mes, dia)
        self.email = email