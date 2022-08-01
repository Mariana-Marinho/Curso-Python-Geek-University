# programa que lê 2 notas de aluno e mostre a média
nota1 = float(input('digite uma nota: '))
nota2 = float(input('digite outra nota: '))
if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
    media = (nota2+nota1)/2
    print(f'a média entre as notas é {media}')
else:
    print('as notas não são válidas')
