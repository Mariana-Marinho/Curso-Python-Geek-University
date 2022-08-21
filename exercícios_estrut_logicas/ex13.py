"""
Média ponderada de uma nota
"""


def ler_numero_positivo(frase):
    while True:
        numero = input(frase)
        try:
            numero = float(numero)
        except:
            print(f'\033[31mdigite um número válido\033[m')
        else:
            return numero


trabalho = ler_numero_positivo('digite sua nota do trabalho: ')
avaliacao = ler_numero_positivo('digite sua nota da prova: ')
final = ler_numero_positivo('digite a nota da sua avaliação final: ')
media = (trabalho*2+avaliacao*3+final*5)/10
if media >= 6:
    print(f'PARABÉNS VOCÊ PASSOU!!!! Sua média ficou {media}')
elif 3 <= media:
    print(f'como sua média foi {media}, você ficou de recuperação...')
else:
    print(f'sua media foi {media}, então você ficou de recuperação')
