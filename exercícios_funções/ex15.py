"""
Se os lados formam triângulo e mostrar que tipo de triângulo
"""


def forms_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[2] < sides[1]+sides[0]:
        return True
    else:
        return False


def triangle_type(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if a == b == c:
        return 'equilátero'
    elif a != b != c:
        return 'escaleno'
    else:
        return 'isósceles'


x, y, z = (float(i) for i in (input('digite os lados do triângulo: ').split()))
if forms_triangle(x, y, z):
    print(f'o triângulo é do tipo {triangle_type(x, y, z)}')
else:
    print('não forma triângulo')
