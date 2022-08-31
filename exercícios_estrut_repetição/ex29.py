"""
Calcular valor da série S = 0 + 1/2! + 2/4! + 3/6!
"""
from math import factorial
S = 0
par = [0, 2, 4, 6, 8]
for i in range(0, 5):
    S += i/factorial(par[i])
    print(f'S({i+1}) = {S}')
