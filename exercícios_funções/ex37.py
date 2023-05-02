"""
Hiperfatorial por série
"""


def hyperfactorial(n):
    fact = 1
    for i in range(n+1):
        fact *= (n**n)*((n-1)**(n-1))
    return fact


x = int(input('digite um número: '))
print(f'o hiperfatorial de {x} vale {hyperfactorial(x)}')
