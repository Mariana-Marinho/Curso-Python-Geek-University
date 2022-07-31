# programa que lê um número positivo e mostre o seu quadrado e sua raiz quadrada
num = float(input('digite um número: '))
if num > 0:
    raiz = num**(1/2)
    quadrado = num**2
    print(f'o quadrado do número {num} equivale a {quadrado}, e sua raiz vale {raiz:.2f}')
else:
    print('digite um número positivo.')
