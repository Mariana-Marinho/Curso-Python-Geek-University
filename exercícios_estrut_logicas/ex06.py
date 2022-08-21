"""
Mostrar o maior número entre dois lidos e a diferença entre eles
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


primeiro = leia_numero('digite um número: ')
segundo = leia_numero('digite outro número: ')
if primeiro > segundo:
    print(f'{primeiro} é maior que {segundo}')
    print(f'{primeiro} - {segundo} = {primeiro-segundo}')
elif primeiro < segundo:
    print(f'{segundo} é maior que {primeiro}')
    print(f'{segundo} - {primeiro} = {segundo-primeiro}')
else:
    print(f'os números são iguais')
