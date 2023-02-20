"""
Gerar matriz 4x4 com valores [1, 20] e transformá-la em triangular inferior
"""
from random import randint

matriz = []
linha_matriz = []

for i in range(4):
    for j in range(4):
        linha_matriz.append(randint(1, 20))
    matriz.append(linha_matriz)
    linha_matriz = []

print('matriz velha: ')
for linha in matriz:
    print(linha)
print()

for i in range(4):
    for j in range(4):
        if j > i:
            matriz[i][j] = 0

print('matriz nova: ')
for linha in matriz:
    print(linha)
