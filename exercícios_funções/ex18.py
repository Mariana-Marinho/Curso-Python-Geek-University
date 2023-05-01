"""
Receber dois valores e retornar x^z
"""


def power(a, b):
    return a**b


print('para a^b')
x = float(input('a: '))
z = float(input('b: '))
print(f'{x}^{z} = {power(x, z)}')
