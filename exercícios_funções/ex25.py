"""
Receber um inteiro positivo e calcular o valor da serie
"""


def serie(number):
    s = 0
    for i in range(number+1):
        s += (number**2 + 1)/(number+3)
    return s


x = int(input('digite um número: '))
print(f'o valor da série é {serie(x)}')
