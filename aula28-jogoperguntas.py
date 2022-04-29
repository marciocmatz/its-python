# Jogo de Perguntas e Respostas:

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '2', 'b': '4', 'c': '6'},
        'resposta_certa': 'b'
        },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 + 3?',
        'respostas': {'a': '2', 'b': '4', 'c': '6'},
        'resposta_certa': 'c'
        },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1 + 1?',
        'respostas': {'a': '2', 'b': '4', 'c': '6'},
        'resposta_certa': 'a'
    }
}

counter_certas = 0

for k, v in perguntas.items():
    print(f'{k} - {v["pergunta"]}')
    for x, y in v['respostas'].items():
        print(f'[{x}] -> {y}')
    resposta_usuario = input('Digite a resposta certa: ')

    if resposta_usuario == v['resposta_certa']:
        print('Você acertou!\n')
        counter_certas += 1
    else:
        print('Você errou!\n')

porcentagem = (counter_certas / len(perguntas) * 100)
print(f'Você acertou {counter_certas} das {len(perguntas)} perguntas e isso representa {porcentagem:.2f}%')
