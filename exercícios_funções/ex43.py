"""
Substituir valores por inteiros, sem repetição
"""
from random import randint


def aleatoriezar(lista):
    new_lista = []
    for i in range(len(lista)):
        new_value = randint(0, len(lista))
        if new_value in new_lista:
            while new_value in new_lista:
                new_value = randint(0, len(lista))
        new_lista.append(new_value)
    return new_lista


LISTA = input('digite valores: ').split()
print(f'a lista randomizada fica: {aleatoriezar(LISTA)}')
