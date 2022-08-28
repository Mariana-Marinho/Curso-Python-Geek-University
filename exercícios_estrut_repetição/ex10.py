"""
Calcular a soma dos 50 primeiros pares
"""
soma = 0
print(f'os 50 primeiros números pares são: ', end='')
for c in range(2, 101, 2):
    print(c, end='...')
    soma += c
print(f'\na soma desses números vale {soma}')
