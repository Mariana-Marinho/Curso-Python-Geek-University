"""
Preencher matriz 4x4 com o produto do valor da linha e da coluna de cada elemento
"""

matriz_velha = []
linha_velha = []
matriz_nova = []
linha_nova = []
produto = produto_linha = 1

for i in range(4):
    for j in range(4):
        linha_velha.append(int(input(f'digite um valor para a {i+1} linha e {j+1} coluna: ')))
    matriz_velha.append(linha_velha)
    linha_velha = []


for i in range(4):
    # produto da linha
    for coluna in range(4):
        produto_linha *= matriz_velha[i][coluna]
    print(f'o produto da linha {i} é {produto_linha}')
    # produto da coluna
    for j in range(4):
        produto = produto_linha
        for linha in range(4):
            # a intersecao ja foi calculada
            if linha != i:
                produto *= matriz_velha[linha][j]
        linha_nova.append(produto)
    produto_linha = 1
    matriz_nova.append(linha_nova)
    linha_nova = []

print('matriz velha: ')
for linha in matriz_velha:
    print(linha)

print('matriz nova: ')
for linha in matriz_nova:
    print(linha)
