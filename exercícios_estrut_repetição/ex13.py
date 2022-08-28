"""
Ler um inteiro e imprimir de 0 ao número, só os pares
"""
digitado = int(input('digite um número: '))
print('pares até esse número: ', end='')
for c in range(2, digitado+1, 2):
    print(c, end='...')
