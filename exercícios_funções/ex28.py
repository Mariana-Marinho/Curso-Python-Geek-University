"""
Valor do cos por serie de taylor
"""
from math import factorial


def cos(x):
    s = 0
    for n in range(0, 50):
        s += (x**(1 + 2*n))/factorial(1 + 2*n)
    return s


angle = float(input('digite o angulo: '))
print(f'o cosseno de {angle} de acordo com a série de Taylor vale {cos(angle)}')
