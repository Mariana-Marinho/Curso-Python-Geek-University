"""
Programa para verificar se um número inteiro é divisível por 3 ou por 5, não simultaneamente
"""


def ler_inteiro(frase):
    while True:
        num = input(frase)
        try:
            num = int(num)
        except Exception as erro:
            print(f'erro ao receber número: {erro}')
        else:
            return num


numero = ler_inteiro('digite um inteiro: ')
if numero % 3 == 0 or numero % 5 == 0:
    if numero % 3 == 0 and numero % 5 != 0:
        print(f'{numero} é divisível por 3, mas não por 5')
    elif numero % 5 == 0 and numero % 3 != 0:
        print(f'{numero} é divisível por 5, mas não por 3')
    else:
        print(f'{numero} é divisível por 3 e por 5')
else:
    print(f'{numero} não é divisível nem por 5 nem por 3')
