# ler um valor inteiro em segundos e imprimir em horas, minutos e segundos
from datetime import timedelta
segundos = float(input('digite os segundos: '))
convertido = timedelta(seconds=segundos)
print(f'{segundos} convertidos para horas e minutos fica {convertido}')
