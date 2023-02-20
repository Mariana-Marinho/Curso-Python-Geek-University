"""
Ler uma matriz 3x3 e imprimir sua transposta
"""
matriz = []
linha_matriz = []

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j}: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

for linha in matriz:
    print(linha)

print('\nmatriz transposta: ')

for j in range(3):
    for i in range(3):
        print(matriz[i][j], end=' ')
    print()
