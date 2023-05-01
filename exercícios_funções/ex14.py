"""
Kilometragem e litros
"""


def print_message(kilometers, liters):
    consume = kilometers / liters
    if consume < 8:
        print('Venda o carro!')
    elif 8 <= consume <= 14:
        print('Econômico!')
    else:
        print('Super econômico!')


km = float(input('digite os km rodados: '))
L = float(input('digite os litros gastos: '))
print_message(km, L)
