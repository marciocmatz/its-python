# Programa para Geração e Validação de CPFs

import random

print()
print('Seja bem-vindo ao CPF Validator 1.0')


while True:
    print()
    print('Selecione uma opção:')
    print('1 - Validar CPF')
    print('2 - Gerar CPF')
    print('3 - Sair')
    opcao = input('->> ')

    if opcao == '1':
        cpf_inputado = input('Digite o CPF: ')
        cpf_limpo = []
        for x in cpf_inputado:
            if x.isnumeric():
                cpf_limpo.append(int(x))

        if len(cpf_limpo) == 11:

            multiplicacao1 = 0
            lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
            for x in range(0, 9):
                multiplicacao1 += cpf_limpo[x] * lista1[x]

            if multiplicacao1 % 11 < 2:
                digito1_calculado = 0
            else:
                digito1_calculado = (11 - (multiplicacao1 % 11))

            multiplicacao2 = 0
            lista2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            for x in range(0, 10):
                multiplicacao2 += cpf_limpo[x] * lista2[x]

            if multiplicacao2 % 11 < 2:
                digito2_calculado = 0
            else:
                digito2_calculado = (11 - (multiplicacao2 % 11))

            if digito1_calculado == cpf_limpo[9] and digito2_calculado == cpf_limpo[10]:
                print('->> CPF VÁLIDO <<-')
            else:
                print('->> CPF INVÁLIDO <<-')
        else:
            print('->> CPF INVÁLIDO <<-')

    elif opcao == '2':
        cpf_aleatorio = []

        for x in range(0, 9):
            cpf_aleatorio.append(random.randint(0, 9))

        multiplicacao1 = 0
        lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        for x in range(0, 9):
            multiplicacao1 += cpf_aleatorio[x] * lista1[x]

        if multiplicacao1 % 11 < 2:
            digito1_calculado = 0
            cpf_aleatorio.append(digito1_calculado)
        else:
            digito1_calculado = (11 - (multiplicacao1 % 11))
            cpf_aleatorio.append(digito1_calculado)

        multiplicacao2 = 0
        lista2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        for x in range(0, 10):
            multiplicacao2 += cpf_aleatorio[x] * lista2[x]

        if multiplicacao2 % 11 < 2:
            digito2_calculado = 0
            cpf_aleatorio.append(digito2_calculado)
        else:
            digito2_calculado = (11 - (multiplicacao2 % 11))
            cpf_aleatorio.append(digito2_calculado)

        cpf_aletorio_final  = ''
        for x in cpf_aleatorio:
            cpf_aletorio_final += str(x)

        print(f'--> CPF GERADO --> {cpf_aletorio_final}')

    elif opcao == '3':
        print('Obrigado!')
        break

    else:
        print('->> OPÇÃO INVÁLIDA <<-')



