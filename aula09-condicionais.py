# if, elif e else

if True:
    print('É verdadeiro')

if 10 > 3:  # A condição a ser analisada precisa retornar um dado do tipo bool.
    print('10 é maior que 3.')


idade = int(input('Digite a sua idade: '))

if idade <= 18:
    print('Você é menor de idade.')
elif idade == 18:
    print('Você tem 18 anos.')
else:
    print('Você é maior de idade.')