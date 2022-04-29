# Criando um programa que valida ou gera CNPJs
from random import randint


def calcula_digito(lista, dig):
    lista_padrao = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    calculo = []
    if dig == 1:
        for x, y in zip(lista, lista_padrao[1::]):
            calculo.append(x * y)
        if sum(calculo) % 11 < 2:
            digito = 0
        else:
            digito = 11 - (sum(calculo) % 11)
        return digito
    if dig == 2:
        for x, y in zip(lista, lista_padrao):
            calculo.append(x * y)
        if sum(calculo) % 11 < 2:
            digito = 0
        else:
            digito = 11 - (sum(calculo) % 11)
        return digito


def is_sequence(cnpj):
    if cnpj == cnpj[0] * 14:
        return True
    else:
        return False


def validar_cnpj():
    cnpj_input = input('Digite o CNPJ que deseja validar (apenas números): ')

    sequencia = is_sequence(cnpj_input)

    if sequencia:
        print('Sequências com todos os números iguais não são válidas.\n')
        return
    else:
        pass

    if cnpj_input.isnumeric() and len(cnpj_input) == 14:
        cnpj_input_list = [int(x) for x in cnpj_input]
        digito2_input = cnpj_input_list.pop()
        digito1_input = cnpj_input_list.pop()

        digito1_calculado = calcula_digito(cnpj_input_list, 1)
        cnpj_input_list.append(digito1_calculado)

        digito2_calculado = calcula_digito(cnpj_input_list, 2)
        cnpj_input_list.append(digito2_calculado)

        if digito1_calculado == digito1_input and digito2_calculado == digito2_input:
            print('>> CNPJ Válido\n')
        else:
            print('>> CNPJ Inválido\n')
    else:
        print('Por favor digite 14 números e apenas números.\n')

    return cnpj_input


def gerar_cnpj():
    cnpj_aleatorio = []
    for x in range(8):
        cnpj_aleatorio.append(randint(0, 8))
    for x in [0, 0, 0, 1]:
        cnpj_aleatorio.append(x)

    digito1_calculado = calcula_digito(cnpj_aleatorio, 1)
    cnpj_aleatorio.append(digito1_calculado)

    digito2_calculado = calcula_digito(cnpj_aleatorio, 2)
    cnpj_aleatorio.append(digito2_calculado)

    cnpj_final = ''
    for x in cnpj_aleatorio:
        cnpj_final += str(x)

    print(f'O CNPJ válido gerado é: {cnpj_final}\n')
    return cnpj_final


print('### Seja bem-vindo ao Gerador/Validador de CNPJs ###')

while True:
    print('Selecione a opção desejada:\n'
          '1 - Gerar CPNJ\n'
          '2 - Validar CNPJ\n'
          '3 - Sair')
    opcao = input('>> ')

    if opcao == '1':
        cnpj = gerar_cnpj()
        with open('log.txt', 'a+') as file:
            file.write(f'Gerado {cnpj}\n')

    elif opcao == '2':
        cnpj = validar_cnpj()
        with open('log.txt', 'a+') as file:
            file.write(f'Validado {cnpj}\n')

    elif opcao == '3':
        print('Obrigado. Programa encerrado.')
        break
    else:
        print('Opção Inválida.\n')
