"""
Calcular hipotenusa
"""


def hypotenuse(a, b):
    h = (a**2 + b**2)**(1/2)
    return h


x, y = (float(x) for x in (input('digite os dois catetos: ').split()))
print(f'a hipotenusa do triângulo cujos catetos são {x} e {y} vale {hypotenuse(x, y)}')
