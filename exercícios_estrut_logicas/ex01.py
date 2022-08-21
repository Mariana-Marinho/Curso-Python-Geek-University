"""
Programa que receba dois números e mostre qual o maior
"""


def leia_numero(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


maior = 0
numeros = [leia_numero('digite um número: '), leia_numero('digite outro número: ')]
for posição, valor in enumerate(numeros):
    if posição == 0 or valor > maior:
        maior = valor
print(f'o maior valor entre {numeros} é {maior}')
