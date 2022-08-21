"""
Receber um número inteiro e verificar se é par ou ímpar
"""


def ler_inteiro(frase):
    while True:
        numero = input(frase)
        try:
            numero = int(numero)
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


num = ler_inteiro('digite um inteiro: ')
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é impar')