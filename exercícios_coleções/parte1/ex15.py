"""
Ler 15 numeros e eliminar repetidos
"""

entradas = []

for i in range(15):
    entradas.append(int(input('digite um valor: ')))

i = 0

while i < len(entradas):
    if i != entradas.index(entradas[i]):
        entradas.pop(i)
    else:
        i += 1

print(entradas)

i = 0
