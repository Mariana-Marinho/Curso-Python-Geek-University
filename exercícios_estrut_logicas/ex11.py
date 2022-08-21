"""
Ler um inteiro positivo e calcular o logaritmo
"""
from math import log10


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
            if numero <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
                continue
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


num = ler_numero_positivo('digite um número positivo: ')
log = log10(num)
print(f'o log do número informado vale {log:.2f}')
