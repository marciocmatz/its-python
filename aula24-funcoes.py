# Funções em Python

def divisao(num1, num2):
    if num2 == 0:
        return
    return num1 / num2

divide = divisao(9, 0)
print(divide)  # None

divide = divisao(9, 3)
print(divide)  # 3.0


# 1:
def daroi(saudacao, nome):
    return f'{saudacao}, {nome}!'

var = daroi('Bem-vindo', 'Marcos')
print(var)


# 2:
def somar(n1, n2, n3):
    return n1 + n2 + n3

soma = somar(1, 2, 3)
print(soma)


# 3:
def perc(n1, percentual):
    return n1 + (n1 * (percentual/100))

acrescimo = perc(150, 10)
print(acrescimo)


# 4:
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 != 0:
        return 'fizz'
    elif num % 5 == 0 and num % 3 != 0:
        return 'buzz'
    elif num % 3 == 0 and num % 5 == 0:
        return 'fizzbuzz'
    else:
        return num

var = fizzbuzz(8)
print(var)
