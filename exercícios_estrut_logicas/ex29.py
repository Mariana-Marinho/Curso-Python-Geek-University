"""
Calcular o preço de um produto, sofrendo alterações
"""
preco_antigo = float(input('digite o valor do produto: '))
if preco_antigo < 50:
    preco_novo = preco_antigo*1.05
elif preco_antigo in range(50, 100):
    preco_novo = preco_antigo*1.1
else:
    preco_novo = preco_antigo*1.15
print(f'o preço novo do produto ficará {preco_novo}, o produto está ', end='')
if preco_novo < 80:
    print('barato')
elif preco_novo in range(80, 120):
    print('normal')
elif preco_novo in range(120, 200):
    print('caro')
else:
    print('muito caro')
