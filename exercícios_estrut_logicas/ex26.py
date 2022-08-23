"""
Somar números inteiros entre 1 e 100
"""
from random import randint

acertou = 0
for i in range(0, 5):
    a = randint(1, 100)
    b = randint(1, 100)
    resposta = int(input(f'qual a soma de {a}+{b}? '))
    if resposta == a+b:
        acertou += 1
    else:
        print(f'a resposta certa era {a+b}')
    print()
print(f'você acertou {acertou} vezes')
