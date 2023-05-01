"""
Quantidade de numeros primos abaixo de n
"""
from sympy import isprime


def quant_primes(number):
    if number >= 2:
        quantity = 1

    if number % 2 == 0:
        number += 1

    for i in range(3, number, 2):
        if isprime(i):
            quantity += 1

    return quantity


x = int(input('digite um numero: '))
print(f'abaixo do numero {x} há {quant_primes(x)} números primos')
