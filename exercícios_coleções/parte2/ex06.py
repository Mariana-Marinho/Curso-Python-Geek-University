"""
Ler duas matrizes 4x4 e preencher uma terceira com o maior valor de cada posição
"""

matriz_A = []
linha_A = []
matriz_B = []
linha_B = []
matriz_final = []
linha_final = []

for i in range(5):
    for j in range(5):
        linha_A.append(int(input(f'matriz A linha {i+1} coluna {j+1}: ')))
    matriz_A.append(linha_A)
    linha_A = []

for i in range(5):
    for j in range(5):
        linha_B.append(int(input(f'matriz B linha {i+1} coluna {j+1}: ')))
    matriz_B.append(linha_B)
    linha_B = []

for i in range(5):
    for j in range(5):
        if matriz_A[i][j] >= matriz_B[i][j]:
            linha_final.append(matriz_A[i][j])
        else:
            linha_final.append(matriz_B[i][j])
    matriz_final.append(linha_final)
    linha_final = []

print('\n Matriz A: ')
for l in matriz_A:
    print(l)

print('\n Matriz B: ')
for l in matriz_B:
    print(l)

print('\n Matriz final: ')
for l in matriz_final:
    print(l)
