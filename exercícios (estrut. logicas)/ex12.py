# calcular a média ponderada de três notas, 1a tem peso 1, a 2a peso 2, a 3a peso 2
nota1 = float(input('digite a sua 1ª nota: '))
nota2 = float(input('digite a sua 2ª nota: '))
nota3 = float(input('digite a sua 3ª nota: '))
if nota1 in range(0, 10) and nota2 in range(0, 10) and nota3 in range(0, 10):
    media = (nota1+nota2+nota3*2)/4
    print(f'a média das notas equivale a {media}')
    if media >= 6:
        print('PARABÉNS!!!!!!! VOCÊ PASSOU')
    else:
        print("""vai ter que estudar mais :'(""")
else:
    print('insira notas válidas')
