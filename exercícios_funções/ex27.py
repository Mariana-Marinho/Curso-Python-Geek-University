"""
calcular série de taylor para seno
"""
from math import pi, factorial


def sin(n):
    s = 0
    for i in range(0, 50):
        s += ((-1) ** i) * (n ** ((2 * i) + 1)) / factorial((2*i) + 1)
    return s


x = float(input('digite um angulo: '))
print(f'o seno de {x} vale {sin(x):.3f}')
