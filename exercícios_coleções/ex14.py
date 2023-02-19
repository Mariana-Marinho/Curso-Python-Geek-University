"""
Ler 10 valores e mostrar os números repetidos
"""
entradas = []

for i in range(10):
    entradas.append(int(input('digite um valor: ')))

print('\nos números repetidos são: ', end='')
for n in range(len(entradas)):
    primeira_ocorrencia = entradas.index(entradas[n])
    if n != primeira_ocorrencia:
        print(f'{entradas[n]}', end='...')
