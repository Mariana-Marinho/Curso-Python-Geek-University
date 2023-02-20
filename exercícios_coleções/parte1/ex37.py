"""
Ordenar elementos de um vetor até o 6 em ordem crescente e depois em ordem derescente
"""

entradas = []
for i in range(11):
    entradas.append(int(input('digite um numero: ')))

# ordem crescente
for m in range(11):
    for n in range(11):
        if entradas[n] > entradas[m]:
            entradas[n], entradas[m] = entradas[m], entradas[n]

i = 1
# jogar numeros alternados para o fim da lista
while i < 6:
    entradas.append(entradas[i])
    entradas.pop(i)
    i += 1

print(entradas)
