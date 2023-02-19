"""
Ler 10 valores ordenando crescente
"""

entradas = []

while len(entradas) < 10:
    valor = int(input('digite um valor: '))
    if len(entradas) == 0:
        entradas.append(valor)

    else:
        for i in range(len(entradas)):
            if entradas[i] >= valor:
                entradas.insert(valor, i)
            elif i == len(entradas) - 1 and valor > entradas[i]:
                entradas.append(valor)


print(entradas)
