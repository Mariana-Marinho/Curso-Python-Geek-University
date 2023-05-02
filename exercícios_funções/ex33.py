"""
Soma dos algarismos do fatorial de um número
"""
from math import factorial


def sum_alg_fact(x):
    s = 0
    fact = str(factorial(x))
    for i in fact:
        s += int(i)
    return s


n = int(input('digite um número: '))
print(f'a soma dos algarismos do fatorial de {n} vale {sum_alg_fact(n)}')
