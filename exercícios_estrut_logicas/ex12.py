"""
Calcular a média ponderada de três notas, 1a tem peso 1, a 2a peso 2, a 3a peso 2
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


nota1 = ler_numero_positivo('digite sua 1ª nota: ')
nota2 = ler_numero_positivo('digite sua 2ª nota: ')
nota3 = ler_numero_positivo('digite sua 3ª nota: ')
media = (nota1 + (nota2*2) + (nota3*2))/5
if media >= 7:
    situacao = 'aprovado'
elif 5 < media:
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'
print(f'a média do aluno foi igual a {media}, está {situacao}')
