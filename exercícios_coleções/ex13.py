"""
Ler 5 valores e mostrar onde tá o maior e o menor
"""

lista = []
for i in range(0, 5):
    num = int(input(f'digite um número para a {i+1}ª posição: '))
    lista.append(num)
print(f'o maior número é o {max(lista)}, e ele está na {lista.index(max(lista))+1}ª posição')
print(f'o menor número é o {min(lista)}, e ele está na {lista.index(min(lista))+1}ª posição')
