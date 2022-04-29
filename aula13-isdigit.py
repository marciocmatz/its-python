num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print('Valores aceitos e convertidos.')
else:
    print('Não posso converter esse tipo de dado para inteiro.')

# Isso não vai ser sempre possível. Para isso vamos precisar lidar com exceções.
# Ou então criamos funções para garantir isso :)
