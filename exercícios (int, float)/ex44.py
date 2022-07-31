# receber a altura do degrau de uma escada e a altura do andar, calcule quantos degraus serão necessários
from math import ceil
degrau = float(input('digite a altura do degrau da escada: '))
altura = float(input('agora digite a altura do andar: '))
# arredondar o número de degraus para cima, pois não há como ter 5.7 degraus, por exemplo, somente 6
escada = ceil(altura/degrau)
print(f'a quantidade de degraus necessária será de {escada}')
