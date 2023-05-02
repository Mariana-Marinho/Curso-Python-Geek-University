"""
retornar fatorial exponencial
"""

def exponencial_factorial(n):
    fact = n
    for i in range(n+1):
        fact **= (n-i)
    return fact


x = int(input('digtie um numero: '))
print(f'o hiperfatorial de {x} vale {exponencial_factorial(x)}')
