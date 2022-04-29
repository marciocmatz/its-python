# Manipulando Arquivos
'''
file = open('teste.txt', 'w')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')
file.close()

file = open('teste.txt', 'r')
lista = []
for x in file.readlines():
    lista.append(x)

print(lista)
'''

with open('teste.txt', 'w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

with open('teste.txt', 'a') as file:
    file.write('Mais uma linha')

with open('teste.txt', 'r') as file:
    print(file.read())
