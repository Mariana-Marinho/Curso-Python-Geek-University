"""
Ler int maior que zero e devolver a soma de todos seus algarismos
"""


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = int(numero)
            if numero <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
                continue
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


num = ler_numero_positivo('digite um número maior que 0: ')
algarismos = str(num)
soma = 0

print('a soma de ', end='')
for i in range(0, len(algarismos)):
    print(num%10, end='...')
    soma += (num % 10)
    num = num//10
print(f' é igual a {soma}')
