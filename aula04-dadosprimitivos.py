# Tipos de dados primitivos:
# str -> strings
# int -> inteiros
# float -> real / ponto flutuante
# bool -> valores lógicos

# Para saber o tipo de dado é preciso usar type()

print(type('String'))
print(type(123456))
print(type(10.80))
print(type(True))

# Conversão comum de ser realizada: string para int/float
print('10', type('10'), type(int('10')))
print(type(float('10.2')))

print('10' + 10)  # Erro dizendo que não pode concatenar string com int
print('10' + '10')  # Vai concatenar e exibir 1010
print(10 + 10)  # Vai exibir 20
