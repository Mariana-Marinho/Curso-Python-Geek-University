"""
Ler inteiro impar e imprimir os ímpares de 1 ao número, ordem decrescente
"""
numero = 2
while numero % 2 != 1:
    numero = int(input('digite um número ímpar: '))
print(f'primeiros {numero} números ímpares: ', end='')
for i in range(numero, 0, -2):
    print(i, end='...')
