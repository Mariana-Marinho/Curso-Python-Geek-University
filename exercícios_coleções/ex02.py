"""
ler 6 inteiros e mostrar na tela os valores lidos
"""
lista = []
for i in range(0, 6):
    num = input(f'digite um valor para a {i+1}ª posição da lista: ')
    lista.append(num)
print(f'os valores digitados foram: {lista}')
