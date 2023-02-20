"""
Ler um vetor de 10 posições e atribuir 0 a todos os valores negativos
"""
entradas = []

for i in range(10):
    entradas.append(int(input(f'digite um numero para a {i+1}ª posição: ')))

print(f'a lista era {entradas}')

for n in range(len(entradas)):
    if entradas[n] < 0:
        entradas[n] = 0

print(f'a lista agora ficou {entradas}')
