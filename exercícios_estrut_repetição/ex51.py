"""
Aumento anual, em 1995 foi contratado por 2000, 1996 aumentou em 1.5%, nos outros anos aumentou ao dobro do ano anterior
"""
from datetime import date
salario = float(input('digite o salário do funcionário: '))
print(f'em 1995 ele ganhava {salario}')
atual = date.today().year
anos = atual - 1995
salario *= 1.015
for c in range(0, anos-1):
    salario *= 1.015
print(f'passados {anos} anos, ele ganhará {salario:.2f} reais em {atual}')
