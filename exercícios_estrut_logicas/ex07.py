"""
Programa que lê 2 notas de aluno e mostre a média
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


nota1 = leia_numero('digite uma nota: ')
nota2 = leia_numero('digite outra nota: ')
media = nota1+nota1/2
print(f'a média do aluno foi igual a {media}')
