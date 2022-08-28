"""
Ler um inteiro e imprimir todos os naturais de 0 ao número
"""
numero = int(input('digite um número: '))
for c in range(0, numero+1):
    print(c, end='...')
