"""
Maior fator primo de um número
"""
from math import sqrt


def highest_prime(number):
    max = 1
    while number % 2 == 0:
        number /= 2
        max = 2

    for i in range(3, int(sqrt(number))+3, 2):
        while number % i == 0:
            max = i
            number //= i
    return max


x = int(input('digite um numero: '))
print(f'{highest_prime(x)} é o maior fator primo de {x}')