"""
Criar dois contadores, um progressivo e um regressivo. 10 elementos.
Tudo dentro de um único laço.
"""

for x in range(0, 10):
    print(x, 10-x)

print()

tamanho = 20
for x in range(0, tamanho + 1):
    print(x, (tamanho - x))
