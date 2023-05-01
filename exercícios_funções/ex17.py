"""
Receber dois inteiros e retornar a soma dos numeros entre eles
"""


def sum_interval(a, b):
    lowest = min(a, b)
    largest = max(a, b)
    soma = 0
    for i in range(lowest+1, largest):
        soma += i
    return soma


x, y = (int(m) for m in (input('digite dois inteiros: ').split()))
print(f'a soma dos inteiros entre {x} e {y} vale {sum_interval(x, y)}')
