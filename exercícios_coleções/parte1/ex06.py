"""
Ler vetor com 10 posições, imprimir o maior e o menor número
"""


def menor(lista):
    menor = 0
    for i in range(0, len(lista)):
        if i == 0:
            menor = lista[i]
        if lista[i] < menor:
            menor = lista[i]
    return menor


def maior(lista):
    maior = 0
    for i in range(0, len(lista)):
        if i == 0:
            maior = lista[i]
        if lista[i] > maior:
            maior = lista[i]
    return maior


numeros = []
for i in range(0, 10):
    while True:
        try:
            x = float(input(f'digite um número para a {i+1}ª posição da lista: '))
        except:
            print('digite um número válido...')
        else:
            numeros.append(x)
            break
print(f'a lista informada foi {numeros}')
print(f'o maior número na lista é {maior(numeros)}')
print(f'o menor número na lista é {menor(numeros)}')
