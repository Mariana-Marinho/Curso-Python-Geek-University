"""
Contar quantas letras seriam usadas se todos os números de 1 a 1000
ex.: de 1 a 10 -> um, dois, três, quatro etc -> 2+4+4+6+5+4+4+4+4+3 = 40
"""
letras = 0
for c in range(0, 1000):
    numero = str(input(f'número {c+1} em palavra: ').strip())
    letras += len(numero)
