# Programação orientada a objetos
'''
class Pessoa:  # Criando a classe

    def __init__(self, nome, idade, comendo=False, falando=False):  # Método construtor da classe
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):  # Método para comer
        if self.comendo:
            print(f'{self.nome} já está comendo {alimento}')
            return

        if self.falando:
            print(f'{self.nome} está falando e não pode comer {alimento}')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo e não pode falar.')
            return
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False


p1 = Pessoa('Luiz', 20)
p1.comer('Maça')
p1.falar('Carros')
p1.parar_comer()
p1.falar('Carros')
p1.comer('Maça')
p1.parar_falar()
p1.comer('Maça')
p1.parar_comer()

p2 = Pessoa('Maria', 23)

p1.comer('Abacate')
p2.comer('Peixe')
'''
from datetime import datetime


class Pessoa:  # Criando a classe

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('João', 23)
p2 = Pessoa('Maria', 18)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
