"""
Próxima jogada num jogo da velha
0 é uma casa vazia, -1 é uma peça minha e 1 é uma peça do oponente
"""
import numpy as np
import random
from time import sleep


jogo_da_velha = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]

vencedor = []


# Check for empty places on board


vazios = []

for i in range(len(jogo_da_velha)):
    for j in range(len(jogo_da_velha)):

        if jogo_da_velha[i][j] == 0:
            vazios.append((i, j))


while len(vazios) != 0:
    atual = random.choice(vazios)
    jogo_da_velha[atual[0]][atual[1]] = -1
    vazios.remove(atual)

    if vazios:
        linha = int(input('linha: '))
        coluna = int(input('coluna: '))
        if (linha, coluna) not in vazios:
            print('digite outros valores...')
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))
        jogo_da_velha[linha][coluna] = 1
        remover = (linha, coluna)
        vazios.remove(remover)

for i in range(3):
    if jogo_da_velha[i][0] == jogo_da_velha[i][1] == jogo_da_velha[i][2]:
        if jogo_da_velha[i][0] == -1:
            vencedor.append('eu')
        else:
            vencedor.append('oponente')

for j in range(3):
    if jogo_da_velha[0][j] == jogo_da_velha[1][j] == jogo_da_velha[2][j]:
        if jogo_da_velha[0][j] == -1:
            vencedor.append('eu')
        else:
            vencedor.append('oponente')

if jogo_da_velha[0][0] == jogo_da_velha[1][1] == jogo_da_velha[2][2]:
    if jogo_da_velha[0][0] == -1:
        vencedor.append('eu')
    else:
        vencedor.append('oponente')

if jogo_da_velha[0][2] == jogo_da_velha[1][1] == jogo_da_velha[2][0]:
    if jogo_da_velha[0][j] == -1:
        vencedor.append('eu')
    else:
        vencedor.append('oponente')


if len(vencedor) > 1:
    if 'oponente' in vencedor and 'eu' in vencedor:
        print('\nhouve um empate')
    elif 'oponente' in vencedor:
        print('\no oponente ganhou')
    else:
        print('\neu ganhei')


print()
for linha in jogo_da_velha:
    print(linha)
