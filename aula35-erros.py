# Como tratar exceções em Python
# A força mais simples de tratar um erro é usar o try except (não é uma boa prática)

try:
    print(a)
except NameError as erro:
    print(erro)

lista = [0, 1]

try:
    print(lista[2])  # IndexError
except IndexError as erro:
    print('Erro:', erro)  # Erro: list index out of range

try:
    print('Teste')
except:
    print('Deu erro')
else:
    print('Não teve erro')


def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Log:', error)
        raise


try:
    print(divide(1, 0))
except ZeroDivisionError as error:
    print(error)

def divisao(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0')
    return n1/n2

divisao(1, 0)
