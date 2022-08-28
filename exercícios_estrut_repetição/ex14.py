"""
Ler um número e imprimir os pares até ao número, só os pares em ordem decrescente
"""
digitado = int(input('digite um número: '))
print(f'os pares de {digitado} a 0: ', end='')
for c in range(digitado, -1, -1):
    if c % 2 == 0:
        print(c, end='...')
