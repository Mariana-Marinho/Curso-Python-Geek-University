"""
Ler vetor com 10 numeros e ordenar
"""

entradas = []

for i in range(10):
    entradas.append(int(input('digite um valor: ')))

for m in range(10):
    for n in range(10):
        if entradas[n] > entradas[m]:
            entradas[n], entradas[m] = entradas[m], entradas[n]

print(entradas)