"""
Ler dois vetores de 10 elementos, criar um com a intersecao dos dois
"""
primeiro = []
segundo = []
intersecao = []

for i in range(10):
    primeiro.append(int(input('digite um valor: ')))

for i in range(10):
    segundo.append(int(input('digite um valor: ')))

for num in primeiro:
    if num in segundo and num not in intersecao:
        intersecao.append(num)

print(f'a interseção é {intersecao}')
