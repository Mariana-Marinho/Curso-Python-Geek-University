# ler um numero, se for positivo retornar a raiz quadrada
num = float(input('digite um número: '))
if num > 0:
    raiz = num**(1/2)
    print(f'a raiz quadrada do número {num} é {raiz:.2f}')
else:
    print('digite um número positivo.')