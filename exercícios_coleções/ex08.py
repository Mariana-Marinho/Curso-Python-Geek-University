"""
Ler 6 valores e imprimí-los em ordem inversa
"""

lista = []
for i in range(0, 6):
    numero = int(input(f'digite um número para a {i+1}ª posição: '))
    lista.append(numero)
lista.reverse()
print('os números informados, em ordem invertida, foram: ')
for numero in lista:
    print(numero, end='...\n')
