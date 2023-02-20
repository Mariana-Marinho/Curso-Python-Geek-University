"""
Ler n e mostrar a n linha do triangulo de pascal
"""
pascal = [1]
linha = [1]

n = int(input('digite um numero para a linha do triangulo de pascal: '))

m = 1

while len(pascal) <= n:
    for i in range(m):

        if i == len(pascal):
            linha.append(1)
        elif i > 0 and i != len(pascal):
            linha.append(pascal[i]+pascal[i-1])

    pascal = linha.copy()
    linha = [1]

    m+=1

print(f'a linha de número {n} no triângulo de pascal vale {pascal}')
