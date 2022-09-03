"""
Diferença entre a soma dos quadrados dos primeiros números naturais e o quadrado da soma
"""
soma_quadrados = 0
quadrado_soma = 0
for i in range(1, 100):
    soma_quadrados += i**2
    quadrado_soma += i
quadrado_soma **= 2
diferenca = quadrado_soma - soma_quadrados
print(f'o quadrado da soma menos a soma dos quadrados dá {diferenca}')
print(f'{quadrado_soma} - {soma_quadrados} = {diferenca}')
