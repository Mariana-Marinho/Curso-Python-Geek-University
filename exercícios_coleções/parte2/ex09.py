"""
Ler uma matriz 3x3 e calcular a soma dos elementos abaixo da diagonal
"""

matriz = []
linha_matriz = []
soma = 0

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j+1}: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

for i in range(3):
    for j in range(3):
        if j < i:
            soma += matriz[i][j]

print()
for lin in matriz:
    print(lin)

print(f'\na soma abaixo da diagonal é {soma}')
