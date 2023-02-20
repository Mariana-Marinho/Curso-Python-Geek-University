"""
Lista de 10 posições, contar e escrever os pares
"""
lista = []
pares = 0
for i in range(0, 10):
    while True:
        try:
            num = float(input(f'digite um número para a {i+1}ª posição: '))
        except Exception:
            print('digite um número')
        else:
            lista.append(num)
            break
print(f'os números informados foram {lista}')
print(f'os números pares da lista são: ', end='')
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        print(lista[i], end='...')
        pares += 1
if pares == 0:
    print('\nnão ter nenhum número par na lista')
else:
    print(f'\ntem {pares} números pares na lista')
