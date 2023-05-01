"""
Triângulo de altura 2*n-1 e largura n
"""


def print_triangle(number):
    for i in range(1, number):
        if i <= number:
            print(f'{"*"*i}')
    for i in range(number+1, 0, -1):
        print(f'{"*"*i}')


x = int(input('qual a altura: '))
print_triangle(x)
