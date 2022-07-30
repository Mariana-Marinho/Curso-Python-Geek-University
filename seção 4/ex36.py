# ler a altura e raio de um cilindro circular e imprimir o volume
from math import pi
raio = float(input('informe o raio do cilindro: '))
altura = float(input('informe a altura do cilindro: '))
volume = raio*raio*pi*altura
print(f'o volume do cilindro informado equivale a {volume}')
