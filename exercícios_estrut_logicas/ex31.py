"""
Calcular o preço de permanência no estacionamento
"""
from math import ceil
entrada_horas = int(input('você entrou de que horas? '))*60
entrada_minutos = int(input('quantos minutos? '))
saida_horas = int(input('você saiu de que horas? '))
saida_minutos = int(input('quantos minutos? '))
minutos = (entrada_horas+entrada_minutos) - (saida_horas+saida_minutos)
horas = ceil(minutos/60)
if horas in range(1, 3):
    print(f'você irá pagar {horas} reais')
elif horas in range(3, 5):
    print(f'você irá pagar {(horas-2)*1.40 + 2} reais')
else:
    print(f'você irá pagar {(horas-4)*2 + 4.8} reais')
