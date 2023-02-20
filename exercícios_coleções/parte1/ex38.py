"""
Ler 10 valores ordenando crescente
"""

entradas = []

while len(entradas) < 10:
    valor = int(input('digite um valor: '))
    if len(entradas) == 0:
        entradas.append(valor)

    else:
        for x in range(len(entradas)):
            if entradas[x] > valor:
                entradas.insert(x, valor)
                break

            elif entradas[x] <= valor and x == len(entradas) - 1:
                entradas.append(valor)

print(entradas)
