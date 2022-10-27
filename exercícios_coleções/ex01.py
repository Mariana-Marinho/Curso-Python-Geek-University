"""
Criar um vetor A que armazene 6 números inteiros
1- atribuir os valores 1, 0, 5, -2, -5, 7
2- somar os valores de A[0], A[1] e A[5]
3- modificar o vetor na posição 4, atribuindo o valor 100
4- mostrar na tela cada valor de A
"""
a = []
a.extend([1, 0, 5, -2, -5, 7])
print(f'''a lista 'a' valia {a}''')
soma = a[0] + a[1] + a[5]
print(f'e a soma dos elementos a[0], a[1] e a[5] valem {a[0]}+{a[1]}+{a[5]} = {soma}')
a[4] = 100
print(f'ponto o número 100 na posição 4, a lista ficará:')
for i in range(0, len(a)):
    print(f'{a[i]:>5}')