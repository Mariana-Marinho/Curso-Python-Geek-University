# ler int maior que zero e devolver a soma de todos seus algarismos
num = input('digite um número inteiro: ')
algarismos = len(num)
num = int(num)
if num > 0:
    i = 0
    soma = 0
    while algarismos > i:
        soma = soma + (num % 10)
        i += 1
        num = num//10
    print(f'a soma dos algarismos do número inserido é {soma}')
else:
    print('digite um inteiro positivo.')
