# 1 - Peça o input de um valor e verifique se ele é par:
num = input('Digite um número inteiro: ')

if num.isdigit():
    num = int(num)
    if (num % 2) == 0:
        print('Você digitou um número par.')
    else:
        print('Você digitou um número impar.')
else:
    print('Você não digitou um número inteiro')

# 2 - Peça o input de uma hora e devolva uma saudação:
hora = int(input('Digite a hora: '))
if hora >= 0 and hora <= 11:
    print('Bom dia.')
elif hora > 11 and hora <= 17:
    print('Boa tarde.')
if hora > 17 and hora < 24:
    print('Boa noite.')

# 3 - Peça o input de um nome e verifique seu tamanho:
nome = input('Digite o seu nome: ')
if len(nome) <= 4:
    print('Seu nome é curto.')
elif 4 < len(nome) <= 6:
    print('Seu nome é médio.')
if len(nome) > 6:
    print('Seu nome é grande.')