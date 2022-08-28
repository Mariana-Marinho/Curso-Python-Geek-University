"""
Ler 10 inteiros e somar sua média
"""
inteiros = []
for i in range(0, 10):
    inteiros.append(int(input('digite um inteiro: ')))
media = sum(inteiros)/10
print(f'a média dos números é igual a {media}')
