"""
Verificar se um número é um quadrado perfetio
"""


def check_perfect_square(number):
    root = number**(1/2)
    if root - int(root) != 0:
        return False
    else:
        return True


x = float(input('digite um número: '))
print(f'o número {x}', 'é um quadrado perfeito' if check_perfect_square(x) else 'não é um quadrado perfeito')
