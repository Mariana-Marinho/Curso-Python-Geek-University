"""
Calcular o número neperiano usando série
"""
from math import factorial


def neperiano(lim):
    l = 0
    for i in range(lim):
        l += 1/factorial(i)
    return l


x = int(input('digite um número para calcular seu neperiano: '))
print(f'o neperiano de {x} é {neperiano(x)}')

