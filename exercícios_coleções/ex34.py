"""
Ler 10 numeros diferentes e botar em vetor
"""

entradas = []

while len(entradas) != 10:
    numero = int(input('digite um valor: '))
    if numero in entradas:
        print('tem que ser diferenteeeeeee')
    else:
        entradas.append(numero)

print(entradas)