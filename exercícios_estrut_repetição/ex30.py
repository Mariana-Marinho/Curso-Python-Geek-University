"""
Calcular sequências
an = 1 + 2 + 3 + ... + n, somar de 1 até n
bn = 1 - 2 + 3 - 4 + 5 - 6 + ... + n, +n se for ímpar, -n se for par
cn = 1 + 3 + 5 + 7 + ... + n, somar até o último ímpar
"""


def an(termo):
    valor = 0
    for i in range(1, termo+1):
        valor += i
    return valor


def bn(termo):
    valor = 0
    for i in range(1, termo+1):
        if i % 2 == 0:
            valor -= i
        else:
            valor += i
    return valor


def cn(termo):
    valor = 0
    for i in range(1, termo+1):
        if i % 2 != 0:
            valor += i
    return valor
