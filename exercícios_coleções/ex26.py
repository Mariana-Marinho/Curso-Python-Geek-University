"""
Calcular desvio padrão de um vetor v contendo 10 números
"""
v = []
somatorio = desvio_padrao = media = 0

for i in range(10):
    v.append(int(input('digite um valor para o vetor v: ')))

media = sum(v) / len(v)

for i in range(len(v)):
    somatorio = (v[i] - media) ** 2

desvio_padrao = ((1/9) * somatorio) ** (1/2)

print(f'o desvio padrão do vetor vale {desvio_padrao}')
