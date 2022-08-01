# mostrar o maior número entre dois lidos e a diferença entre eles
num1 = float(input('digite um número: '))
num2 = float(input('digite outro: '))
if num1 > num2:
    print(f'o maior número é {num1}, e a diferença é {num1-num2}')
elif num1 == num2:
    print('os números são iguais, digite outros.')
else:
    print(f'o maior número é {num2}, e a diferença é {num2-num1}')
