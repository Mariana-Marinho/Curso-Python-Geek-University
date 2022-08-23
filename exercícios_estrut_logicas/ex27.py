"""
Classificar uma pessoa entre altura e peso
"""

peso = float(input('digite o peso em kg: '))
altura = float(input('digite a altura em metros: '))
if peso < 60:
    if altura < 1.2:
        print('categoria A')
    elif 1.2 <= altura < 1.7:
        print('categoria B')
    else:
        print('categoria C')
elif peso in range(60, 90):
    if altura < 1.2:
        print('categoria D')
    elif 1.2 <= altura < 1.7:
        print('categoria E')
    else:
        print('categoria F')
else:
    if altura < 1.2:
        print('categoria G')
    elif 1.2 <= altura < 1.7:
        print('categoria H')
    else:
        print('categoria I')
