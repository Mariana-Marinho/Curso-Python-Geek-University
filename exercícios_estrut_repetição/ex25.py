"""
Somar todos os números naturais abaixo de 100 que são múltiplos de 3 ou 5
"""


def dividindo(num, div):
    if num % div == 0:
        return True
    else:
        return False


soma = 0
print('somando ', end='')
for numero in range(1, 1001):
    if dividindo(numero, 3) or dividindo(numero, 5):
        soma += numero
        print(numero, end='...')
print(f'\na soma deu {soma}')
