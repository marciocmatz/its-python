# Input serve para pegar dados através da entrada do usuário

nome = input('Qual o seu nome? ')
print(f'O usuário digitou: {nome} e tipo do dado é {type(nome)}')
# A entrada de um input sempre será do tipo string.

# É possível realizar a conversão das variáveis já na entrada:
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número:' ))

print(num1 + num2)