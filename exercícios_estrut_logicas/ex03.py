"""
Ler um número real, se foi positivo imprimir a raiz quadrada, se for negativo o quadrado
"""


def ler_numero(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
            if numero == 0:
                print(f'\033[31mdigite um número diferente de 0\033[m')
                continue
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


num = ler_numero('digite um valor: ')
if num > 0:
    raiz = num**(1/2)
    print(f'raiz de {num} = {raiz:.2f}')
else:
    quadrado = num**2
    print(f'{num}² = {quadrado}')
