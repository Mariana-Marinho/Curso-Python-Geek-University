"""
Ler 10 inteiros e botar em vetor, escrever os primos e suas posições
"""

entradas = []
primos = []

for i in range(10):
    entradas.append(int(input('digite um valor para o vetor: ')))

for i in range(len(entradas)):
    if entradas[i] > 1:
        parametro = entradas[i]-1

        while parametro > 1:
            if entradas[i] % parametro == 0:
                parametro = -1
            else:
                parametro -= 1

        if entradas[i] not in primos and parametro == 1:
            primos.append(entradas[i])

print('os numeros primos são: ', end='')

for num in primos:
    print(f'{num}, na {entradas.index(num)}ª posição  ', end='.......')
