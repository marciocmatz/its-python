# Split, Join e Enumerate

# split()
# A função split amarzena os valores em uma lista.

texto = 'O Brasil é o país do futebol. O Brasil é o país do futuro.'

print(texto.split())  # ['O', 'Brasil', 'é', 'o', 'país', 'do', 'futebol.', 'O', 'Brasil', 'é', 'o', ...
print(texto.split('.'))  # ['O Brasil é o país do futebol', ' O Brasil é o país do futuro', '']

''''''

# join()
# Transfootma uma lista em string

lista1 = ['a', 'b', 'c', 'd']
teste = ''
print(teste.join(lista1))  # abcd

''''''

#  enumerate()
#  A função enumerate enumera cada elemento de uma lista (começa do 0)

for v1, v2 in enumerate(lista1):
    print(v1, v2)

lista2 = [[1, 2, 3], [4, 5, 6]]
for v1, v2 in enumerate(lista2):
    print(v1, v2)