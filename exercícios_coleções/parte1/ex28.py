"""
Ler 10 inteiros e botar em vetor, criar v1 e v2
impares para v1 e pares para v2
"""
v = []
v1_impares = []
v2_pares = []

for i in range(10):
    v.append(int(input('digite um valor: ')))

for num in v:
    if num % 2 == 0 and num not in v2_pares:
        v2_pares.append(num)
    elif num % 2 != 0 and num not in v1_impares:
        v1_impares.append(num)

print('números impares: ', end='')
for num in v1_impares:
    print(num, end='...')

print('\nnumeros pares: ', end='')
for num in v2_pares:
    print(num, end='...')
