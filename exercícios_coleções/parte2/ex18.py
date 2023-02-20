"""
Matriz 3x3 e somar os valores da coluna
"""

matriz = []
linha_matriz = []

somas = []
soma = 0

for i in range(3):
    for j in range(3):
        linha_matriz.append(int(input(f'linha {i+1} coluna {j+1}: ')))
    matriz.append(linha_matriz)
    linha_matriz = []

for j in range(3):
    for i in range(3):
        soma += matriz[i][j]
    somas.append(soma)
    soma = 0

print()
for linha in matriz:
    print(linha)
print()

print(somas)
