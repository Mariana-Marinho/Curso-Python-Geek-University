"""
Ler 10 inteiros positivos ignorando não positivos
"""
inteiros = []
while len(inteiros) <= 10:
    digitado = int(input('digite um inteiro: '))
    if digitado > 0:
        inteiros.append(digitado)
media = sum(inteiros)/10
print(f'a media dos números inseridos é igual a {media}')
