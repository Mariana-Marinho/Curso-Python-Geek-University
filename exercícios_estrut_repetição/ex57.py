"""
Quantos números primos existem entre a e b
"""


def ler_primo(numero):
    for c in range(2, numero):
        if numero == c:
            # caso ele for 2
            return True
        elif numero % c == 0:
            return False
    return True


inicio = int(input('início do intervalo: '))
final = int(input('final do intervalo: '))
quantidade = 0
for i in range(inicio, final+1):
    if ler_primo(i):
        quantidade += 1
print(f'entre {inicio} e {final} há {quantidade} números primos')
