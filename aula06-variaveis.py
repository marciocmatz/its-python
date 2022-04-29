# Variáveis servem para armazenar dados em memória.
# Não se pode iniciar com números. Para separar nomes usar _. Não se pode iniciar com letras maiscúlas.
# Python tem tipagem dinâmica.

nome = 'Draven'
idade = 21
altura = 1.80
e_maior = idade > 18
peso = 82

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('É maior?: ', e_maior)

imc = peso / (altura * altura)
print(f'Seu nome é {nome} e seu IMC é {imc}')
