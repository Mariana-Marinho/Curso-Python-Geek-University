"""
Vetor de inteiros e retorne quantos pares ele possui
"""


def even_quant(lista):
    quant = 0
    for i in lista:
        if int(i) % 2 == 0 and int(i) != 0:
            quant += 1
    return quant


x = input('digite alguns números: ').split()
print(f'foram digitados {even_quant(x)} números pares')
