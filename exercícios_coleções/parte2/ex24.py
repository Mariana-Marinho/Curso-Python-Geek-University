"""
Matriz 20x20, achar o maior produto de 4 números adjacentes
"""


def maior_produto(matrix):
    if len(matrix) > 3 or len(matrix[0]) > 3:
        maior_prod = 0
        linha, coluna = len(matrix[0]), len(matrix)
        for x in range(linha):
            for y in range(coluna):
                # busca horizontal
                if (x+3) < linha:
                    prod = matrix[x][y]*matrix[x+1][y]*matrix[x+2][y]*matrix[x+3][y]
                    maior_prod = max(prod, 0)

                # busca vertical
                if (y+3) < coluna:
                    prod = matrix[x][y] * matrix[x][y + 1] * matrix[x][y + 2] * matrix[x][y + 3]
                    maior_prod = max(prod, 0)

                # busca diagonal
                if (x+3) < linha and (y+3) < coluna:
                    prod = matrix[x][y] * matrix[x + 1][y + 1] * matrix[x + 2][y + 2] * matrix[x + 3][y + 3]
                    maior_prod = max(prod, 0)

                # busca anti-diagonal
                if x >= 3 and (x+3) < linha and (y+3) < coluna:
                    prod = matrix[x][y] * matrix[x - 1][y + 1] * matrix[x - 2][y + 2] * matrix[x - 3][y + 3]
                    maior_prod = max(prod, 0)

        return maior_prod

    else:
        return 0


matriz = []
linha_matriz = []

for i in range(20):
    for j in range(20):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j+1}= ')))
    matriz.append(linha_matriz)
    linha_matriz = []


print(f'o maior produto é {maior_produto(matriz)}')
