# Dicionários
import copy

dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
}

v = copy.deepcopy(dicionario)
v['chave1'] = 'valorNovo'

print(dicionario)  # {'chave1': 'valor1', 'chave2': 'valor2'}
print(v)  # {'chave1': 'valorNovo', 'chave2': 'valor2'}