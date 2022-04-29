# Formatação de strings: f-strings e format.

nome = 'Draven'
idade = 23
altura = 1.90
e_maior = idade > 18
peso = 90
imc = peso / (altura ** 2)

print(f'Seu nome é {nome}, você tem {idade} anos de idade. Seu IMC é: {imc:.2f}.')  # F-strings
# Para exibir apenas as casas decimais que você quiser é só usar :.xf, como está na linha acima.

print('{} tem {} anos de idade e seu IMC é {:.2f}.'.format(nome, idade, imc))  # Format
# Usar a f-strings é mais fácil e prático.