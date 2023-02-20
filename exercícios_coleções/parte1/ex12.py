"""
Ler 5 valores, mostrá-los, maior, menor e média
"""


def ler_maior(lista):
    maior = 0
    for numero in lista:
        if numero > maior or lista.index(numero) == 0:
            maior = numero
    return maior


def ler_menor(lista):
    menor = 0
    for numero in lista:
        if numero < menor or lista.index(numero) == 0:
            menor = numero
    return menor


numeros = []
for i in range(0, 5):
    num = int(input('digite um valor: '))
    numeros.append(num)
media = sum(numeros)/len(numeros)
print(f'o maior número da lista é {ler_maior(numeros)}')
print(f'o menor número da lista foi {ler_menor(numeros)}')
print(f'a média foi {media}')
