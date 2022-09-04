"""
Número aleatório entre 1 e 1000, informar se o aleatório é maior ou menor
"""
from random import randint

aleatorio = randint(1, 1000)
while True:
    chute = int(input('chute um número entre 1 e 1000: '))
    if chute < aleatorio:
        print('aumente o chute...\n')
    elif chute > aleatorio:
        print('eita, o número é menor\n')
    else:
        print('PARABÉNSSS VOCÊ ACERTOU!!!!')
        break
