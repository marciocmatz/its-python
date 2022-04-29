from functools import reduce

produtos = [
    {'produto': 'p1', 'preco': 20.00},
    {'produto': 'p2', 'preco': 10.00},
    {'produto': 'p3', 'preco': 30.00},
    {'produto': 'p4', 'preco': 22.00},
    {'produto': 'p5', 'preco': 15.00},
    {'produto': 'p6', 'preco': 17.00},
    {'produto': 'p7', 'preco': 8.00}
]

soma_precos = reduce(lambda ac, item: ac + item['preco'], produtos, 0)
print(soma_precos)

print(f'A média de preços é {soma_precos/len(produtos):.3f}')  # 17.429
