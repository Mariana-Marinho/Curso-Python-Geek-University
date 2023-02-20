"""
Ler uma matriz 4x4 e retornar a posicao do maior valor
"""

matriz = []
linha_matriz = []
linha = coluna = 0

for i in range(4):
    for j in range(4):
        linha_matriz.append(int(input(f'digite um valor para a {i+1} linha e {j+1} coluna: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

maior = matriz[0][0]

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linha = i
            coluna = j

for linha in matriz:
    print(linha)

print(f'o maior numero informado foi {maior} na {linha+1} linha e {coluna+1} coluna')
