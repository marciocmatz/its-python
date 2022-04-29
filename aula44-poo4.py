# Encapsulamento
# Esconder partes do código?

# public, protect, private

class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    def inserir(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listar(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir(1, 'Draven')
bd.inserir(2, 'Lucian')
bd.inserir(3, 'Nocturne')

bd.listar()

bd.apagar(2)
bd.listar()

