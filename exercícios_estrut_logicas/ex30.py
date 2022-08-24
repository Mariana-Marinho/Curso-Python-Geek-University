"""
Leia uma data e determine se é valida
"""


def data(dia, mes, ano):
    if dia in range(1, 31) and mes in range(1, 13) and 0 <= ano:
        if (ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)) and mes == 2:
            # ano bissexto e mês fevereiro
            if dia in range(1, 30):
                return True
            else:
                return False
        elif mes == 2:
            if dia in range(1, 29):
                return True
            else:
                return False
        elif mes in (1, 3, 5, 7, 9, 11):
            if dia in range(1, 31):
                return True
            else:
                return False
        else:
            if dia in range(1, 30):
                return True
            else:
                return False
    else:
        return False


d = int(input('digite o dia: '))
m = int(input('digite o mês: '))
a = int(input('digite o ano: '))
if data(d, m, a):
    print(f'{d}/{m}/{a} é uma data válida')
else:
    print(f'{d}/{m}/{a} não é uma data válida')
