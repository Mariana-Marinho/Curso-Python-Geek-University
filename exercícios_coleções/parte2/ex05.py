"""
Ler uma matriz 5x5, ler um valor x e encontrá-lo na matriz
"""

matriz = []
linha_matriz = []
linha = coluna = -1

for i in range(5):
    for j in range(5):
        linha_matriz.append(int(input(f'linha {i+1} e coluna {j+1}: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

n = int(input('digite um numero para procurá-lo: '))

for i in range(5):
    for j in range(5):
        if matriz[i][j] == n:
            linha = i
            coluna = j

print()
for l in matriz:
    print(l)
print()

if linha < 0 or coluna < 0:
    print(' o número não está na matriz')

else:
    print(f'o numero {n} está na {linha+1} linha e {coluna+1} coluna')
