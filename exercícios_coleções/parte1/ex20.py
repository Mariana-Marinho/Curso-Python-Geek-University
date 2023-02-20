"""
Ler inteiros de 0~50 e por num vetor de 10 posicoes
segunda lista com valores impares, imprimir com 2 elementos por linha
"""

entradas = []
impares = []

while len(entradas) != 5:
    entrada = int(input('digite um valor: '))
    if entrada in range(0, 51):
        entradas.append(entrada)
    else:
        print('digite um numero entre 0 e 50\n')

for num in entradas:
    if num % 2 != 0 and num not in impares:
        impares.append(num)

impares = sorted(impares)

print('entradas | impar')
for n in range(len(entradas)):
    print(entradas[n], end=' | ')
    if n in range(len(impares)):
        print(impares[n])
    else:
        print()
