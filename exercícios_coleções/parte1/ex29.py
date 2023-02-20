"""
Ler 6 inteiros e mostras os pares, a soma, os ímpares e a quantidade de impares
"""

entradas = []
pares = []
impares = []

for i in range(6):
    entradas.append(int(input('digite um valor: ')))

for num in entradas:
    if num % 2 == 0 and num not in pares:
        pares.append(num)

    elif num % 2 != 0 and num not in impares:
        impares.append(num)

print(f'os números pares foram {pares} e a soma deles dá {sum(pares)}')
print(f'foram {len(impares)} números ímpares: {impares}')
