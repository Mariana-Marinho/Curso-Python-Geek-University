# ler um número real, se foi positivo imprimir a raiz quadrada, se for negativo o quadrado
num = float(input('digite um número: '))
if num > 0:
    raiz = num**(1/2)
    print(f'a raiz quadrada de {num} equivale a {raiz:.2f}')
elif num < 0:
    quadrado = num**2
    print(f'o quadrado do número {num} equivale a {quadrado}')
else:
    print('digite um número diferente de 0')
