# and or not in

if 2 == 2 and 3 != 2:
    print('Verdadeiro 1')
if 2 == 2 or 3 != 2:
    print('Verdadeiro 2')

if 'a' in 'Draven':
    print(f'Tem a letra "a" na palavra "Draven"')

if 'a' not in 'Draven':
    print(f'Não tem a letra "a" na palavra "Draven"')
elif 'a' in 'Draven':
    print(f'Tem a letra "a" na palavra "Draven"')

a = ''
if not a:  # O not é bastamte usado pra ver se uma variável tem ou não conteúdo.
    print('a não tem valor algum')

print('-------')
usuario = input('Nome de usuário: ')
senha = input('Senha: ')

if usuario == 'usuario1' and senha == '123456':
    print('Seja bem-vindo.')
elif usuario != 'usuario1' and senha == '123456':
    print('Usuário Incorreto.')
elif usuario == 'usuario1' and senha != '123456':
    print('Senha Incorreta.')
