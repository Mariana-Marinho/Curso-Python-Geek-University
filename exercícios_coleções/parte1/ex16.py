"""
Ler um vetor de 5 posiçoes e um codigo
se o codigo for 0 finalizar o programa
se for 1 mostrar a lista em ordem inversa
se for 2 mostrar a lista em ordem normal
"""
entradas = []

for n in range(5):
    entradas.append(int(input(f'digite um numero para a {n+1}ª posição: ')))

codigo = int(input('\nMENU:\n'
                   '0 - finalizar o programa\n'
                   '1- mostrar a lista em ordem inversa\n'
                   '2- mostrar a lista em ordem direta\n'
                   'sua escolha: '))
print()
while codigo != 0:
    print()
    if codigo == 1:
        print(f'a lista era {entradas}')
        # printar em ordem inversa com slice
        print(f'em ordem inversa fica: {entradas[::-1]}')

    elif codigo == 2:
        print(f'a lista em ordem direta é {entradas}')

    else:
        print('digite um código válido...')

    codigo = int(input('\nMENU:\n'
                       '0 - finalizar o programa\n'
                       '1- mostrar a lista em ordem inversa\n'
                       '2- mostrar a lista em ordem direta\n'
                       'sua escolha: '))

print('\ncódigo finalizado')
