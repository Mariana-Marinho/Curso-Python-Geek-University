"""
Recebe a data atual e exibe na tela em forma de texto
"""
import datetime


def get_month(mes):
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro'
    }
    return meses.get(mes)


def get_date(day, month, year):
    month = get_month(month)
    return f'{day} de {month} de {year}'

y, m, d = str(datetime.date.today()).split('-')
y = int(y)
m = int(m)
d = int(d)
print(f'Data: {get_date(d, m, y)}')
