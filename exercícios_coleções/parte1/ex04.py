"""
Lista de 8 posições,
valores de x e y na lista em outra lista
soma de x e y
"""
lista = []
selecionados = []
soma = 0
for i in range(0, 8):
    lista.append(input(f'digite um valor para a {i+1}ª posição da lista:'))
print()
while True:
    x = float(input('digite um valor para verificar se ele está na lista'))
    if x in lista:
        print(f'{x} está na lista')
        selecionados.append(x)
        soma += x
        if len(selecionados) == 2:
            break
    else:
        print(f'{x} não está na lista')
print()
print(f'os números informado foram: {lista}')
print(f'os números selecionados foram {selecionados}, e a soma deles dá {soma}')
