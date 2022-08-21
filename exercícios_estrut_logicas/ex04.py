"""
Programa que lê um número positivo e mostre o seu quadrado e sua raiz quadrada
"""


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
            if numero <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
                continue
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


num = ler_numero_positivo('digite um número: ')
raiz = num**(1/2)
quadrado = num**2
print(f'raiz de {num} = {raiz}')
print(f'{num}² = {quadrado}')