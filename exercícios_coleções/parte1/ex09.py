"""
Ler 6 valores pares, mostrar em ordem invertida
"""


def ler_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


lista = []
while True:
    num = int(input('digite um valor par: '))
    if ler_par(num):
        lista.append(num)
        if len(lista) == 6:
            break
print('\nos valores informados, em ordem inversa, foram: ', end='')
for numero in lista:
    print(numero, end='...')
