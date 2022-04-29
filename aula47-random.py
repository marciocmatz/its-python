import random
import string

var1 = random.randint(10, 20)  # Número inteiro entre 10 e 20
print(var1)

var2 = random.uniform(10, 20)  # Número flutuante entre 10 e 20
print(f'{var2:.2f}')  # Setei pra ter duas casas decimais só

var3 = random.random()  # Número flutuante entre 0 e 1
print(var3)

nomes = ['jose', 'lucas', 'marcos', 'luis']
print(random.choice(nomes))  # Escolhe algo aleatório dentro de uma sequência

random.shuffle(nomes)  # Faz uma mudança de posições dentro da lista (ele altera o dado original, cuidado).
print(nomes)

# Gerando senhas aleatórias
letras = string.ascii_letters
digitos = string.digits
caracteres = '@#$%&*()_-'
geral = letras + digitos + caracteres

senha = ''.join(random.choices(geral, k=10))
print(f'A senha gerada é {senha}')
