# Listas são, junto com dicionários, as estruturas de dados mais importantes do Python.
"""
Listas podem ser acessadas por indices da mesma maneira que strings
Em listas é possível mudar um elemento através do seu indice

append = coloca um elemento no final da lista
insert = insere um elemento através do seu indice (acaba mudando o indice dos outros elementos da lista)
pop = exclui o ultimo elemento da lista
del = exclui elementos da lista através do seu indice
clear = limpa a lista toda
extend = coloca os valores de uma lista dentro de outra lista


min = retorna o menor valor de uma lista
max = retorna o maior valor de uma lista

range =
"""
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista = list(range(1, 10)) -> outra forma de criar essa lista 

lista.append(10)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista.pop()  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.insert(3, 'banana')  # [1, 2, 3, 'banana', 4, 5, 6, 7, 8, 9]
del(lista[3])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista.clear()  # []
"""

secreto = 'perfume'
tem = []

while True:
    letra = input('digite uma letra: ')
    if letra in secreto:
        tem.append(letra)
    else:
        print('n tem essa letra')
    exibir = ''
    for x in secreto:
        if x in tem:
            exibir += x
        else:
            exibir += '#'

    print(exibir)

