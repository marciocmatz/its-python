# Zip e Zip_longest
from itertools import zip_longest

citys = ['São Paulo', 'Santos', 'Rio de Janeiro', 'Curitiba']
states = ['SP', 'SP', 'RJ']

city_state = zip_longest(citys, states, fillvalue='SEM ESTADO')

for valor in city_state:
    print(valor)

# Somando duas listas com zip:
lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 8, 4]


soma = []
for x, y in zip(lista1, lista2):
    soma.append(x + y)
print(soma)
# ---------------
soma2 = [x + y for x, y in zip(lista1, lista2)]
print(soma2)