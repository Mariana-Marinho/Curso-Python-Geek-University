"""
Ler um vetor com 15 posicoes e tirar os 0
"""

entradas = []
for i in range(15):
    entradas.append(int(input('digite um valor: ')))

for num in entradas:
    if num == 0:
        entradas.remove(num)

print(entradas)
