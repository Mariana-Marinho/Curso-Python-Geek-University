"""
Ler dois vetors de 10 posições
criar vetor com valores do primeiro nas posicoes pares e valores do segundo nas posicoes impares
"""

primeiro = []
segundo = []
terceiro = []

for i in range(10):
    primeiro.append(int(input('digite um valor para o primeiro vetor: ')))

for i in range(10):
    segundo.append(int(input('digite um valor para o segundo vetor: ')))

for i in range(len(primeiro)):
    if len(terceiro) % 2 == 0:
        # se o vetor tiver um tamanho par, a proxima posicao é par
        terceiro.append(primeiro[i])
    else:
        terceiro.append(segundo[i])

print(terceiro)
