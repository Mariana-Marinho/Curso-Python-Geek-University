"""
Inteiro positivo e retornar a soma dos algarismos
"""


def sum_algarisms(number):
    soma = 0
    for i in number:
        soma += int(i)
    return soma


x = input('digite um inteiro positivo: ')
print(f'a soma dos algarismos de {x} vale {sum_algarisms(x)}')
