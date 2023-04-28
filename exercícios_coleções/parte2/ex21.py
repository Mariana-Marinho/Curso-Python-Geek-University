"""
Ler duas matrizes 2x2, e botar um menu:
1) somar as duas matrizes
2) subtrair a primeira da segunda
3) adicionar uma constante às duas matrizes
4) imprimir as matrizes
"""

matriz_1 = []
linha_matriz_1 = []
matriz_2 = []
linha_matriz_2 = []

for i in range(2):
    for j in range(2):
        linha_matriz_1.append(float(input(f'matriz 1: linha {i+1} coluna {j+1}: ')))
    matriz_1.append(linha_matriz_1)
    linha_matriz_1 = []

for i in range(2):
    for j in range(2):
        linha_matriz_2.append(float(input(f'matriz 2: linha {i+1} coluna {j+1}: ')))
    matriz_2.append(linha_matriz_2)
    linha_matriz_2 = []

entrada = int(input('escolha de 1 a 5: '))

while entrada != 5:
    if entrada == 1:
        print(f'\n\n soma das matrizes: ')
        for i in range(2):
            for j in range(2):
                print(matriz_1[i][j] + matriz_2[i][j], end='   ')
            print()

    elif entrada == 2:
        print(f'\n\n subtrair a primeira da segunda: ')
        for i in range(2):
            for j in range(2):
                print(matriz_2[i][j] - matriz_1[i][j], end='   ')
            print()

    elif entrada == 3:
        print('\n\n adicionar constante as duas matrizes: ')
        constante = float(input('digite uma constante para as duas matrizes: '))
        print('matriz 1:')
        for i in range(2):
            for j in range(2):
                print(matriz_1[i][j] * constante, end='  ')
            print()
        print('matriz 2:')
        for i in range(2):
            for j in range(2):
                print(matriz_2[i][j] * constante, end='  ')
            print()

    else:
        print('\n\nimprimir as duas matrizes: ')
        print('\nmatriz 1: ')
        for linha in matriz_1:
            print(linha)
        print('\nmatriz 2: ')
        for linha in matriz_2:
            print(linha)

    entrada = int(input('\n\n\nescolha de 1 a 5: '))

print('\n\nprograma finalizado')
