"""
Somar divisores de um número
"""
while True:
    try:
        numero = int(input('digite um número: '))
        if numero >= 1:
            break
    except Exception as erro:
        print(f'Erro: {erro}')
soma = 0
print(f'a soma dos divisores do número {numero} é: ', end='')
for div in range(1, numero):
    if numero % div == 0:
        soma += div
        print(f' + {div}' if div != 1 else f'{div}', end='')
print(f' = {soma}')
