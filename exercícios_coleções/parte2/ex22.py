"""
Ler duas matrizes 3x3 e calcular C = A*B
"""

matriz_A = []
matriz_B = []
matriz_final = []
linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'matriz A, linha {i+1} coluna {j+1}: ')))
    matriz_A.append(linha_matriz)
    linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'matriz B, linha {i+1} coluna {j+1}: ')))
    matriz_B.append(linha_matriz)
    linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(matriz_A[i][j] * matriz_B[j][i])
    matriz_final.append(linha_matriz)
    linha_matriz = []

print('\nmatriz A: ')
for linha in matriz_A:
    print(linha)

print('\nmatriz B: ')
for linha in matriz_B:
    print(linha)

print('\nmatriz final: ')
for linha in matriz_final:
    print(linha)
