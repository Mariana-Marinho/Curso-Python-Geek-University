"""
Ler matriz 3x6 com reais
- somar elementos de colunas impares
- media da 2a e 4a colunas
- substituir os valores da 6a coluna pela soma da coluna 1 e 2
- imprimir a matriz modificada
"""

matriz = []
linha_matriz = []

impares = media = 0

for i in range(3):
    for j in range(6):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j+1}: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

print('matriz velha: ')
for linha in matriz:
    print(linha)
print()

for i in range(3):
    for j in range(6):
        # se for uma coluna impar
        if j % 2 == 0:
            impares += matriz[i][j]
        # colunas 2 e 4
        if j == 1 or j == 3:
            media += matriz[i][j]
        # 6a coluna
        if j == 5:
            matriz[i][j] = matriz[i][1] + matriz[i][2]

print('matriz nova: ')
for linha in matriz:
    print(linha)
print()

print(f'a soma das colunas ímpares deu: {impares}')
print(f'a média da segunda e quarta colunas deus {media/6}')
