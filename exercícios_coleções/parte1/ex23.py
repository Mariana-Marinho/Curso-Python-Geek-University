"""
Ler dois vetores de 5 posições e criar um vetor com o produto vetorial
"""
primeiro = []
segundo = []
produto_escalar = []
valor = 0

for i in range(5):
    primeiro.append(int(input('digite um valor para o primeiro vetor: ')))

for i in range(5):
    segundo.append(int(input('digite um valor para o segundo vetor: ')))

for i in range(5):
    valor += primeiro[i] * segundo[i]
    produto_escalar.append(valor)

print(f'o produto escalar ficou: {produto_escalar}')
