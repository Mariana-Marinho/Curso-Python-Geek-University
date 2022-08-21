"""
Verificar se 3 valores podem ser lados de triângulos, se sim, classificar
"""
lados = []

for i in range(0, 3):
    lado = float(input('digite um lado do triângulo: '))
    lados.append(lado)
lados.sort(reverse=True)
# para haver triângulo, o lado maior tem que ser menor que a soma dos outros 2 lados
if sum(lados)-max(lados) > max(lados):
    print('triângulo pode ser formado, e ele será um triângulo ', end='')
    if lados[0] == lados[1] == lados[2]:
        print('equilátero')
    elif lados[1] == lados[2]:
        print('isósceles')
    else:
        print('escaleno')
else:
    print(f'não é possível formar triângulo')
