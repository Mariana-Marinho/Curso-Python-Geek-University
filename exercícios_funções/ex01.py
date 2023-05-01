"""
Função que retorna o dobro
"""


def dobro(x):
    """
    Retorna o dobro de um número
    :param x: número que se deseja dobrar
    :return: dobro de x
    """
    return 2*x

num = int(input('digite um número: '))
print(f'o dobro de {num} vale {dobro(num)}')
