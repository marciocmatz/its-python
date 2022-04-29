import json

d1 = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': '25',
    },
    'Pessoa 2': {
        'nome': 'Ana',
        'idade': '22',
    },
}

d1_json = json.dumps(d1)  # Converte o dicionário para JSON

with open('teste.json', 'w') as file:  # Vamos gravar esse json dentro de um arquivo json
    file.write(d1_json)

with open('teste.json', 'r') as file:  # Vamos abrir esse json para usar em algo dentro do code
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Aqui é feita a conversão de json para dicionario
    print(d1_json)