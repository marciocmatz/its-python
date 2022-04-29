"""
While - Enquanto

while condicao:
    code ...
"""

# Tomar cuidado com o while pra não criar um loop infinito...
# while True:
#    print('ok')

# continue = vai pular um bloco de execução
# break = finaliza o loop, mas continua caso tenha mais code fora do loop

# Junto com o laço while é possível usar else, assim como no if
# O else vai ser executado assim que a condição do while se tornar falsa

x = 0
while x < 10:
    print(x)
    x += 1
else:
    print('cheguei no else')

# O else não vai ser executado caso exista um break dentro do while. Só vai ser executado caso a condição do while se
# tornar falsa.
