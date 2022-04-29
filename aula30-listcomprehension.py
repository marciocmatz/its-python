#List Comphension

lista = list(range(100))
listaNova = [x if x % 3 == 0 else 0 for x in lista]

print(listaNova)  # [0, 24, 48, 72, 96]


# Exercício

string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
lista = [string[i:i + n] for i in range(0, len(string), n)]
print(lista)

retorno = '.'.join(lista)
print(retorno)