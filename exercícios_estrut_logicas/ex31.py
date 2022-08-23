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

entrada = input('de que horas você entrou? HH:MM\n').strip().split()
for time in entrada:
    hour, minu = [int(i) for i in time.split(":")]
    print(hour, "hours and", minu, "minutes")
    print(classmethod(hour))
