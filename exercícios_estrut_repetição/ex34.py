"""
Calcular o menor número divisível para cada um dos números de 1 a 20
"""

numero = contador = 1
while True:
    for div in range(2, 21):
        if numero % div != 0:
            numero += 1
            continue
        else:
            contador += 1
    if contador == 21:
        print(numero)
