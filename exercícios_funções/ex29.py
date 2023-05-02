"""
Seno hiperbólico por serie de taylor
"""
from math import factorial


def hyperbolic_sin(x):
    s = 0
    for n in range(0, 50):
        s += (x**(1 + 2*n)) / factorial(1 + 2*n)
    return s


angle = float(input('digite o angulo: '))
print(f'o seno hiérbólico de {angle} vale {hyperbolic_sin(angle)}')
