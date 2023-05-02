"""
Retorna o maior valor
"""


def highest(lista):
    big = float(lista[0])
    for i in lista[1:]:
        i = float(i)
        if i > big:
            big = i
    return big


LISTA = input('digite alguns números: ').split()
print(f'o maior número digitado foi {highest(LISTA)}')
