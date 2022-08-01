# ler um inteiro positivo e calcular o logaritmo
from math import log10
num = int(input('digite um inteiro positivo: '))
if num > 0:
    log = log10(num)
    print(f'o log do número informado vale {log:.2f}')
else:
    print('insira um número válido')
