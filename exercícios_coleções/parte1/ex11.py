"""
Ler 10 reais, quantos negativos e soma dos positivos
"""

lista = []
negativos = 0
positivos = 0
for i in range(0, 10):
    num = float(input(f'digite o {i+1}º valor: '))
    lista.append(num)
for numero in lista:
    if numero >= 0:
        positivos += numero
    else:
        negativos += 1
print(f'foram digitados {negativos} negativos e a soma dos positivos deu {positivos}')
