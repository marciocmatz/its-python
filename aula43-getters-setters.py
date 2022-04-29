# Getters e Setters
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))  # O certo é usar REGEX aqui
        self._preco = valor


p1 = Produto('camiseta', 'R$50')
p1.desconto(10)
print(p1.preco)
'''


class Produto:

    def __init__(self, preco):
        self.preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco.replace('R$', '')


p1 = Produto('R$30')
print(p1.preco)