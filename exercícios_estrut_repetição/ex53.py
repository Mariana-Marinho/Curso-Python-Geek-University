"""
Ler um inteiro positivo e imprimir n linhas do triângulo de floyd
"""
linhas = int(input('quantas linhas do Triângulo de Floyd? '))
termo = 1
for l in range(0, linhas+1):
    print()
    for i in range(0, l):
        print(termo, end=' ')
        termo += 1
