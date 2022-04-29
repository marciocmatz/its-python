# Desempacotamento de listas

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

n1, n2, *resto_lista = lista
print(n1, n2, resto_lista)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

n1, n2, *resto_lista, ultimo_valor = lista
print(n1, n2, resto_lista, ultimo_valor)  # 0 1 [2, 3, 4, 5, 6, 7, 8] 9

*resto_lista, n1, n2, n3 = lista
print(resto_lista, n1, n2, n3)  # [0, 1, 2, 3, 4, 5, 6] 7 8 9

# Trocando valores entre variáveis
x = 10
y = 'Draven'

x, y = y, x  # Basta fazer isso! Vale para 3, 4 ... valores.
print(x)
print(y)
