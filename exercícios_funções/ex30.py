"""
Calcular o cosseno hiperbólico de um ângulo
"""
from math import factorial


def hyperbolic_cos(x):
    s = 0
    for n in range(0, 50):
        s += (x**(2*n)) / factorial(2*n)
    return s


angle = float(input('digite um valor:'))
print(f'o valor do cosseno hiperbólico de {angle} vale {hyperbolic_cos(angle)}')
