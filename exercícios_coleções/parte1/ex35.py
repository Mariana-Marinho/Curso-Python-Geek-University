"""
Ler dois numeros a e b ]0, 10000[
vetor onde cada posição é um algarismo do numero
"""
soma = []

a = int(input('digite um numero: '))
b = int(input('digite outro numero: '))

posicao_a = list(str(a))
if len(posicao_a) < 5:
    valor = 5 - len(posicao_a)
    for i in range(valor):
        posicao_a.insert(0, 0)

posicao_b = list(str(b))
if len(posicao_b) < 5:
    valor = 5 - len(posicao_b)
    for i in range(valor):
        posicao_b.insert(0, 0)

for i in range(5):
    soma.append(posicao_a[i] + posicao_b[i])
