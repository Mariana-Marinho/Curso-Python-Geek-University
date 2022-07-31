# receber um número inteiro e verificar se é par ou ímpar
num = float(input('digite um número: '))
if num == 0:
    print('digite um número diferente de 0')
elif num % 2 == 0:
    print(f'o número {num} é par')
else:
    print(f'o número {num} é ímpar')
