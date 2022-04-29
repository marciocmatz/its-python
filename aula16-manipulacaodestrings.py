# Manipulação de strings
# Fatiamento e índices

texto = 'Olá, seja bem-vindo'

print(texto[1])  # l
print(texto[0:10])  # Olá, seja
print(texto[0::2])  # Oá eabmvno

print(texto[-1])  # o

"""
O python começa seu indice em 0. Quando usamos os indices pra fatiar uma string, é importante saber que o último
caractere não é incluido no retorno. Ou seja, para pegar algo até o 10 caractere é preciso passar o índice 11.

string[começo : fim : passo]  // Por padrão o passo é igual a 0

"""