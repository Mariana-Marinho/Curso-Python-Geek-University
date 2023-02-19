"""
Ler 5 valores e mostrar onde tá o maior e o menor
"""

entradas = []
for i in range(10):
    entradas.append(int(input('digite um valor: ')))

maior = menor = entradas[0]

for num in entradas:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f'o maior número é {maior} e está na {entradas.index(maior)+1}ª posição')
print(f'o menor número é {menor} e está na {entradas.index(menor)+1}ª posição')
