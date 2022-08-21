"""
Calcular a área de um trapézio, recebendo base maior, base menor e altura
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


print('CALCULAR ÁREA DE TRAPÉSIO\n')
base_maior = ler_numero_positivo('digite o valor da base maior em cm: ')
base_menor = ler_numero_positivo('digite o valor da base menor em cm: ')
altura = ler_numero_positivo('digite a altura: ')
area = ((base_maior+base_menor)*altura)/2
print(f'o trapézio com as características informadas tem área de {area}cm²')
