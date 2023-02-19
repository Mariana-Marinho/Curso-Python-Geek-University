"""
Ler dois vetores x e y com 5 inteiros sem repetidos
1 - mostrar soma de x e y
2 - produto de x e y
3 - diferenca de x e y
4 - intersecao de x e y
5 - uniao de x e y
"""

x = []
y = []
intersecao = []
uniao = []

for i in range(5):
    x.append(int(input('digite um valor: ')))

for i in range(5):
    y.append(int(input('digite um valor: ')))

escolha = int(input('escolha de 1 a 5: '))

if escolha == 1:
    print('a soma dos valores é: ', end='')
    for i in range(5):
        print(f'{x[i]} + {y[i]} = {x[i] + y[i]}', end='...........')
    print()

elif escolha == 2:
    print('o produto dos valores é: ', end='')
    for i in range(5):
        print(f'{x[i]} * {y[i]} = {x[i] * y[i]}', end='...........')
    print()

elif escolha == 3:
    print('a diferença dos valores é: ')
    for i in range(5):
        if x[i] not in y:
            print(f'{x[i]} - {y[i]} = {x[i] - y[i]}', end='...........')
        print()

elif escolha == 4:
    print('a interseção é: ', end='')
    intersecao = [num for num in x if num in y]
    print(intersecao)
    print()

else:
    # escolha == 5
    print(f'a união é: ', end='')
    uniao = [num for num in x]
    uniao = uniao + [num for num in y if num not in uniao]
    print(uniao)
    print()

