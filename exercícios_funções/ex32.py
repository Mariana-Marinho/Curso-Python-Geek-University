"""
Simplificar fração
"""

def simplify(a, b):
    frase = ''
    for i in range(2,  min(a, b)+1):
        if a%i == b%i == 0:
            numerador = int(a/i)
            denominador = int(b/i)
            frase = f'{numerador}/{denominador}'
    return frase


print('para x/y, digite: ')
x = int(input('x: '))
y = int(input('y: '))
print(f'a simplificação de {x}/{y} vale {simplify(x, y)}')
