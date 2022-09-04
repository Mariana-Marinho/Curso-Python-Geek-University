"""
Ler um inteiro positivo e imprimir a soma dos n primeiros números primos
"""


def ler_primo(numero):
    for c in range(2, numero):
        if num == c:
            #caso ele for 2
            return True
        elif num % c == 0:
            return False

    return True


vezes = int(input('quantas vezes deseja somar? '))
num = 2
soma = contador = 0
while contador < vezes:
    if ler_primo(num):
        soma += num
        print(num, end='...')
        contador += 1
    num += 1
print(f'\na soma deu {soma}')
