"""
Lançamento de dois dados n vezes e sair a relação entre os dois números
"""
from random import randint
vezes = int(input('quantas vezes deseja jogar? '))
for c in range(0, vezes):
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print(f'o primeiro dado de {d1} e o segundo deu {d2}')
    if d1 > d2:
        print(f'{d1} > {d2}')
    elif d1 < d2:
        print(f'{d1} < {d2}')
    else:
        print(f'{d1} = {d2}')
