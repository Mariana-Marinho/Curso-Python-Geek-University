"""
Gerar triângulo de altura n e base 2n-1
"""


def print_triangle(number):
    for i in range(1, 2*number, 2):
        print(f'{"*"*i}')


x = int(input('digite um número: '))
print_triangle(x)
