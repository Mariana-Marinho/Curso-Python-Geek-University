"""
Ler um inteiro e imprimir de 0 ao número, em ordem decrescente
"""
numero = int(input('digite um número: '))
for c in range(numero, -1, -1):
    print(c, end='...')
