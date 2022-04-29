# Jogo de Advinhação de Palavras
import random

num_linha = random.randint(0, 3)
palavra_secreta = ''
with open('palavras.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    palavra_secreta_aux = linhas[num_linha]

tamanho = len(palavra_secreta_aux) - 1

for x in range(0, tamanho):
    palavra_secreta += palavra_secreta_aux[x]


letras_digitadas = []
vidas = 3
temporario = ''

print(f'A palavra secreta tem {len(palavra_secreta)} letras e você tem {vidas} vidas.')
print('*' * len(palavra_secreta))

while temporario != palavra_secreta:
    print()
    letra = input('Digite uma letra: ')

    if len(letra) == 1:
        letras_digitadas.append(letra.upper())
    else:
        print('Digite apenas uma letra!')
        letra = ''

    if letra.upper() not in palavra_secreta:
        vidas -= 1

    temporario = ''
    for x in palavra_secreta:
        if x in letras_digitadas:
            temporario += x
        else:
            temporario += '*'

    print(f'Palavra ->> {temporario}')
    print(f'Vidas ->> {vidas}')

    if vidas == 0:
        print()
        print('VOCÊ PERDEU TODAS AS VIDAS. BOA SORTE NA PRÓXIMA!')
        print(f'A PALAVRA ERA >> {palavra_secreta} <<')
        break

else:
    print()
    print('PARABÉNS! VOCÊ ACERTOU A PALAVRA SECRETA.')
    print(f'->> {palavra_secreta} <<-')