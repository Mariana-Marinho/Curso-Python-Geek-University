"""
Calcular sequência Fibonacci
"""
numero = int(input('quantos números da sequência informados? '))
a = 0
b = 1
i = 0
for c in range(numero+1):
    if c > 1:
        f = a + b
        a = b
        b = f
        print(f'{f}', end='...')
    else:
        print(f'{i}', end='...')
        i += 1
