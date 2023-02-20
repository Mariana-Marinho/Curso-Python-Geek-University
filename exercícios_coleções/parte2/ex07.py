"""
Preencher uma matriz 10x10
"""

matriz = []
linha_matriz = []

for i in range(10):
    for j in range(10):
        if i < j:
            linha_matriz.append( 2*i + 7*j - 2 )
        elif i > j:
            linha_matriz.append( 4*(i**3) - 5*(j**2) + 1 )
        else:
            linha_matriz.append( 3*(i**2) - 1 )
    matriz.append(linha_matriz)
    linha_matriz = []

for lin in matriz:
    print(lin)
