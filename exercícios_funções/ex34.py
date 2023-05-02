"""
Função não recursiva para calcular fatorial duplo
"""

def double_factorial(x):
    fact = 1
    for i in range(1, x+1, 2):
        fact *= i
    return fact


number = int(input('digite um inteiro ímpar: '))
print(f'o fatorial duplo de {number} vale {double_factorial(number)}')
