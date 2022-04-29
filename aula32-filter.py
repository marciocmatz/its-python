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

# Filtando só pessoas que tem mais de 22 anos de idade:
maiores_22 = []
for x in filter(lambda pessoa: pessoa['idade'] > 22, pessoas):
    maiores_22.append(x)
print(maiores_22)
