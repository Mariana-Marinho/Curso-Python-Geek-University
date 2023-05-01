"""
Função que verifica se um numero é positivo ou negativo
"""


def neg_or_pos(number):
    if number >= 0:
        return 1
    else:
        return 0


x = float(input('digite um número: '))
print(f'o número {x} é', 'positivo' if neg_or_pos(x) == 1 else 'negativo')
