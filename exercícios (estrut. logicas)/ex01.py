# programa que recebe dois números e mostra qual o maior
num1 = float(input('digite um número: '))
num2 = float(input('digite outro número: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 == num2:
    print(f'os números são iguais')
else:
    print(f'{num2} é maior que {num1}')
