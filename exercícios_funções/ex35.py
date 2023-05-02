"""
Função não recursiva que recebe um n e calcula o fatorial quadruplo
"""
from math import factorial


def fourth_factorial(n):
    fact = factorial(2*n)/factorial(n)
    return fact


x = int(input('digite um numero: '))
print(f'o fatorial quádruplo de {x} vale {fourth_factorial(x)}')
