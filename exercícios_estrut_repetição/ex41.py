"""
Calcular associação em paralelo de dois resistores
"""
res_1 = float(input('Primeiro resistor (em Ohms): '))
res_2 = float(input('Segundo resistor (em Ohms): '))
resistividade = (res_1*res_2) / (res_1+res_2)
print(f'a resistividade total numa associação em paralelo dos dois resistores é {resistividade} Ohm')
