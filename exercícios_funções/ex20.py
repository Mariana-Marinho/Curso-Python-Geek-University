"""
Fatorial de um número
"""


def factorial(number):
    fact = 1
    for i in range(2, number+1):
        fact *= i
    return fact


x = int(input('digite um numero: '))
print(f'o fatorial de {x} é {factorial(x)}')
