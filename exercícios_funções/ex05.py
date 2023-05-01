"""
Volume de uma esfera
"""
from math import pi


def sphere_volume(radius):
    volume = 4/3 * (radius**3) * pi
    return volume


r = float(input('digite o raio da esfera: '))
print(f'o volume da esfera de raio {r} é {sphere_volume(r):.2f}')
