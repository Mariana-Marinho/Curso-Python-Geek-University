"""
Trocar valor
"""


def trocar(a, b):
    a, b = b, a
    return f'a: {a} , b: {b}'


x, y = input('digite dois numeros para a e b: ').split()
print(trocar(x, y))
