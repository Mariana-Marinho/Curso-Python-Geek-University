"""
Soma de 1 a n
"""


def soma(n):
    s = 0
    for i in range(n+1):
        s += i
    return s


x = int(input('digite um valor: '))
print(f'a soma de 1 a {x} vale {soma(x)}')
