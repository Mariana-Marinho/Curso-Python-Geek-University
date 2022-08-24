"""
Listar divisores de um número ou dizer se é primo caso não existam divisores
"""
numero = int(input('número: '))
print(f'{numero} é divisível por ', end='')
d = 0
for i in range(1, numero+1):
    if numero % i == 0:
        print(f'{i}...', end='')
        d += 1
if d == 2:
    print('\né um número primo')
else:
    print('\nnão é primo')
