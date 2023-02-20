"""
Ler dois vetores de 10 posições, o primeiro com notas e o segundo com alturas
encontrar as alturas mais alta e mais baixa e suas notas
"""

notas = []
alturas = []

for i in range(5):
    notas.append(float(input(f'digite a nota do {i+1}º aluno: ')))
    alturas.append(float(input(f'digite a altura do {i+1}º aluno: ')))

menor = maior = alturas[0]

for altura in alturas:
    if altura > maior:
        maior = altura
    if altura < menor:
        menor = altura

print(f'\no maior aluno tem {maior}m e sua nota foi {notas[alturas.index(maior)]}')
print(f'o menor aluno tem {menor}m e sua nota foi {notas[alturas.index(menor)]}')

