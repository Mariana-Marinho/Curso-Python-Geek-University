"""
Ler números e imprimir o maior valor e quantas vezes foi lido
"""
quant = int(input('quantos números deseja por? '))
numeros = []
for i in range(0, quant):
    numeros.append(int(input(f'digite o {i+1}º número: ')))
maior = max(numeros)
c = 0
for i in numeros:
    if i == maior:
        c += 1
print(f'O maior número digitado foi o {maior}, e apareceu {c} vezes')
