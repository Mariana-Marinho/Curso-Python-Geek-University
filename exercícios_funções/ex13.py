"""
Receber dois valores e um símbolo
"""


def operation(a, b, operator):
    if operator == '/':
        return a/b
    elif operator == '*':
        return a*b
    elif operator == '-':
        return a-b
    else:
        return a+b


x = float(input('digite um numero: '))
y = float(input('digite outro numero: '))
operador = float(input('digite o operador: '))
print(f'{x}{operador}{y} = {operation(x, y, operador)}')
