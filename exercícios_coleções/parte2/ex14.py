"""
Gerar um número entre 0 e 99 e botar em matriz 5x5, sem repetir
"""
from random import randint

matriz = []
linha_matriz = []
bingo = []

for i in range(5):
    for j in range(5):
        numero = randint(0, 99)
        while numero in bingo:
            numero = randint(0, 99)
        linha_matriz.append(numero)
        bingo.append(numero)
    matriz.append(linha_matriz)
    linha_matriz = []

for linha in matriz:
    print(linha)
