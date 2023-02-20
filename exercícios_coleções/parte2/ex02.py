"""
Matriz 5x5, preencher a diagonal com 1 e o resto com 0
"""

matriz = []
linha = []

for i in range(5):
    for j in range(5):
        if i == j:
            linha.insert(j, 1)
        else:
            linha.insert(j, 0)
    matriz.append(linha)
    linha = []

for linha in matriz:
    print(linha)
