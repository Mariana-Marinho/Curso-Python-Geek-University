"""
Ler uma matrix 4x4 e escrever quantos valores maiores que 10 ela possui
"""

matriz = []
linha = []
maiores = 0

for i in range(4):
    for j in range(4):
        elemento = int(input(f'digite um valor para o elemento na linha {i+1} na coluna {j+1}: '))
        linha.append(elemento)
    matriz.append(linha)
    linha = []

for linha in matriz:
    for numero in linha:
        if numero > 10:
            maiores += 1

print(f'a matriz possui {maiores} números maiores que 10')
