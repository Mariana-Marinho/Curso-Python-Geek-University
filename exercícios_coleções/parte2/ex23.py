"""
Ler uma matriz 3x3 e calcular uma B = A²
"""

matriz_A = []
matriz_final = []
linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j+1}: ')))
    matriz_A.append(linha_matriz)
    linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(matriz_A[i][j] * matriz_A[j][i])
    matriz_final.append(linha_matriz)
    linha_matriz = []

print('\nmatriz A: ')
for linha in matriz_A:
    print(linha)

print('\n matriz final: ')
for linha in matriz_final:
    print(linha)
