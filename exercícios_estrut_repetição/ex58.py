"""
Soma entre os números primos entre a e b
"""


def ler_primo(numero):
    for i in range(2, numero):
        if numero == 1:
            return True
        elif numero % i == 0:
            return False
    return True


soma = 0
inicio = int(input('digite o início do intervalo: '))
final = int(input('digite o fim do intervalo: '))
for n in range(inicio, final+1):
    if ler_primo(n):
        soma += n
print(f'a soma dos números primos entre {inicio} e {final} dá {soma}')
