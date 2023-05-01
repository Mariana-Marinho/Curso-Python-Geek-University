"""
Retornar qual número é o maior
"""


def get_largest(x, y):
    if x > y:
        return x
    else:
        return y


a, b = (float(i) for i in (input('digite dois números: ').split()))
print(f'o maior número entre {a} e {b} é {get_largest(a, b)}')
