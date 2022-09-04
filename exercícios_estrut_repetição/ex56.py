"""
Somar todos os números primos abaixo de um milhão
"""


def ler_primo(numero):
    for c in range(2, numero):
        if num == c:
            # caso ele for 2
            return True
        elif num % c == 0:
            return False
    return True


soma = 0
for num in range(2, 1_000_000):
    if ler_primo(num):
        soma += num
        print(num, end='...')
print(f'\na soma dos primos abaixo de 1 milhão é igual a {soma}')