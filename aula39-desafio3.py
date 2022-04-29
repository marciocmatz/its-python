# Crie uma lista de tarefas com as seguintes opções:
# Adicionar tarefas, listar tarefas, desfazer e refazer

print('Olá, seja bem vindo ao seu controle de tarefas!')
print('Selecione a opção desejada:')
print('1 - Adicionar Tarefa\n'
      '2 - Vizualizar Tarefas\n'
      '3 - Desfazer\n'
      '4 - Refazer\n'
      '5 - Sair\n')

tarefas = []
ultima_tarefa = []

while True:

    opcao = input('Digite a opção: ')

    if opcao == '1':
        tarefas.append(input('Digite o nome da tarefa: '))
        print('Tarefa adicionada.\n')

    elif opcao == '2':
        for indice, tarefa in enumerate(tarefas):
            print(f'Tarefa {indice + 1}: {tarefa}')
        print()

    elif opcao == '3':
        try:
            ultima_tarefa.append(tarefas.pop())
            print(f'A tarefa *{ultima_tarefa[-1]}* foi removida da lista de tarefas.\n')
        except:
            print('Não existe item na lista de tarefas.\n')

    elif opcao == '4':
        try:
            tarefas.append(ultima_tarefa[-1])
            print(f'A tarefa *{ultima_tarefa[-1]}* foi adicionada a lista de tarefas.\n')
            ultima_tarefa.pop()
        except:
            print('Não existe itens para desfazer.\n')

    elif opcao == '5':
        print('Obrigado. Programa Encerrado.')
        break

    else:
        print('Opção Inválida.\n')
