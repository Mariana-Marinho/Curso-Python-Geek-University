"""
Receber horas, minutos e segundos e converter em segundos
"""


def set_seconds(hours, minutes, seconds):
    return hours*360 + minutes*60 + seconds


h, m, s = (int(x) for x in input('digite as horas, minutos e segundos: ').split())
print(f'isso tudo vale {set_seconds(h, m, s)} segundos')
