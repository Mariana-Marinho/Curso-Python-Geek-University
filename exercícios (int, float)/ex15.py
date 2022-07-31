# ler um ângulo em rad e converter em graus
from math import degrees
rad = float(input('digite o ângulo em rad: '))
graus = degrees(rad)
print(f'{rad:.2f}rad equivale a {graus:.2f}°')
