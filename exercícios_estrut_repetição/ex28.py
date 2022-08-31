"""
Ler um número e calcular E, sendo E= 1 + 1/1! + 1/2! + ... + 1/n!
"""
from math import factorial
while True:
    try:
        numero = int(input('digite um número inteiro positivo: '))
        break
    except Exception as erro:
        print(f'ERROR: {erro}')
E = 1
for i in range(1, numero+1):
    E += 1/factorial(i)
print(f'sendo E = 1 + 1/1! + 1/2! + ... + 1/n!, E({numero}) = {E:.4f}')
