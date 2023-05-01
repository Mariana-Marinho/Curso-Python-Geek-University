"""
Volume do cilindro
"""
from math import pi


def cylinder_volume(height, radius):
    v = height * (radius ** 2 * pi)
    return v


HEIGHT = float(input('digite a altura do cilindro: '))
RADIUS = float(input('digite o raio do cilindro: '))
print(f'o volume do cilindro cuja altura é {HEIGHT} e raio é {RADIUS} vale {cylinder_volume(HEIGHT, RADIUS)}')
