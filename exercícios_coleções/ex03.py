"""
Ler números reais, botar em lista e calcular o quadrado, botando em outro valor
"""


numeros = []
quadrados = []
for i in range(0, 10):
    num = float(input('digite um número para calcular seu quadrado: '))
    numeros.append(num)
    quadrados.append(num**2)
print(f'{"NÚMERO":<15}', end='')
print(f'{"QUADRADO":>15}')
for i in range(0, 10):
    print(f'{numeros[i]:<15}', end='')
    print(f'{quadrados[i]:>15}')
