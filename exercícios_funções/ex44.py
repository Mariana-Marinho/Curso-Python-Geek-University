"""
retornar pares e impares
"""


def even_uneven(lista):
    even = []
    uneven = []
    for v in lista:
        if float(v) % 2 == 0:
            even.append(v)
        else:
            uneven.append(v)
    return set(even), set(uneven)


LISTA = input('digite alguns valores: ').split()
pares, impares = even_uneven(LISTA)
print(f'os pares são {pares} e os impares são {impares}')
