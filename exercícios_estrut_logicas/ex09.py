"""
Programa que receba a altura e sexo de alguém e mostrar seu peso ideal conforme IMC
"""


def leia_numero(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
            if numero <= 0:
                print(f'\033[31mdigite um número maior que 0\033[m')
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


altura = leia_numero('digite sua altura em cm: ')
while True:
    sexo = input('seu sexo é feminino ou masculino? [FEM/MASC] ')
    if sexo.upper() in "MASC":
        imc = (0.727*altura)-58
        print(f'seu peso ideal equivale a {imc:.2f}kg')
        break
    elif sexo.upper() in "FEM":
        imc = (0.621*altura)-44.7
        print(f'seu peso ideal é {imc:.2f}kg')
        break
    else:
        print('\033[31mdigite feminino/masculino\033[m')
