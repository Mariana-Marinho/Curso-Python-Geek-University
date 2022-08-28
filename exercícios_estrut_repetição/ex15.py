"""
Ler um número ímpar e imprimir os ímpares de 1 ao número, crescente
"""
digitado = 2
while digitado % 2 == 0:
    digitado = int(input('digite um número ímpar: '))
print(f'os ímpares de 1 a {digitado}: ', end='')
for c in range(1, digitado+1, 2):
    print(c, end='...')
