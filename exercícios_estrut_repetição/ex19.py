"""
Ler inteiro entre 100 e 999 e imprimir casa um dos algarismos do número
"""


def mil(n):
    if (n // 10) // 10 != 0:
        return True
    else:
        return False


numero = 1
while mil(numero) is False:
    numero = int(input('digite um algarismo com 3 classes: '))
for c in range(0, 3):
    print(numero % 10)
    numero = numero // 10
