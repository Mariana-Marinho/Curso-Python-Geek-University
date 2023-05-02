"""
Função não recursiva que retorna superfatorial
"""
from math import factorial


def superfactorial(n):
    fact = 1
    for i in range(n+1):
        fact *= factorial(i)
    return fact


x = int(input('digite um inteiro: '))
print(f'o superfatorial de {x} vale {superfactorial(x)}')
