"""
Ler um número, se for positivo, retornar a raiz
"""


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
            if numero <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
            else:
                return numero
        except:
            print(f'\033[31mdigite um número válido\033[m')


num = ler_numero_positivo('digite um número: ')
raiz = num**(1/2)
print(f'a raiz quadrada do número {num} é {raiz:.2f}')
