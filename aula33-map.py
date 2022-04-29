
produtos = [
    {'produto': 'p1', 'preco': 20.00},
    {'produto': 'p2', 'preco': 10.00},
    {'produto': 'p3', 'preco': 30.00},
    {'produto': 'p4', 'preco': 22.00},
    {'produto': 'p5', 'preco': 15.00},
    {'produto': 'p6', 'preco': 17.00},
    {'produto': 'p7', 'preco': 8.00}
]

pessoas = [
    {'nome': 'Jose', 'idade': 20},
    {'nome': 'Lucas', 'idade': 22},
    {'nome': 'Alfredo', 'idade': 17},
    {'nome': 'Maria', 'idade': 23},
    {'nome': 'Bruna', 'idade': 25},
    {'nome': 'Bianca', 'idade': 26},
]


def aumenta_preco(p):
    p['preco'] = p['preco'] * 1.05
    return p


produtos_com_acrescimo = map(aumenta_preco, produtos)

for item in produtos_com_acrescimo:
    print(item)


def coloca_silva(nome):
    nome['nome'] = f'{nome["nome"]} Silva'
    return nome

novos_nomes = map(coloca_silva, pessoas)

for item in novos_nomes:
    print(item)

so_nomes = [x['nome'] for x in pessoas]
print(so_nomes)