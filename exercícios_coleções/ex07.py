"""
Ler 10 inteiros e botar em lista, mostrar ela o maior e a index dele
"""

lista = []
for i in range(0, 10):
    num = int(input(f'digite um número para a {i+1}ª posição: '))
    lista.append(num)
print(f'os números informados foram: ', end='')
for numero in lista:
    print(numero, end='...')
maior = max(lista)
print(f'\no maior número foi o {maior}, ele esta na {lista.index(maior)+1}ª posição')
