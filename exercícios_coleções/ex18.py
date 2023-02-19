"""
Ler 10 valores, ler x e contar os multiplos de x
"""
entradas = []
multiplos = []

for i in range(10):
    entradas.append(int(input(f'digite um valor para a {i+1}ª posição: ')))

x = int(input('\ndigite um valor x: '))

for num in entradas:
    if num % x == 0 and num not in multiplos:
        multiplos.append(num)

print(f'\nos multiplos de {x} na lista são {multiplos}')
