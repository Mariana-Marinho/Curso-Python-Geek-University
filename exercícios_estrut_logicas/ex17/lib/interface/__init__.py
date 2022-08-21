"""
Validação do que o usuário digita e interface do menu
"""


def menu(opcoes):
    print('_'*15)
    print(f'{"MENU":^15}')
    print('_'*15)
    for i, v in enumerate(opcoes):
        print(f'{i+1}- {v}')
    while True:
        escolha = ler_numero_positivo('sua escolha: ')
        if escolha in range(1, len(opcoes)+1):
            break
    return escolha


def ler_numero_positivo(frase):
    while True:
        num = input(frase)
        try:
            num = int(num)
            if num <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
                continue
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return num


def ler_numero_qualquer(frase):
    while True:
        num = input(frase)
        try:
            num = float(num)
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return num
