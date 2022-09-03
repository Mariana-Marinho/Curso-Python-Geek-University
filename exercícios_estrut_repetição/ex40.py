"""
Ler vários números, para quando ler negativo e imprimir o maior e o menor lidos
"""
numeros = []
while True:
    valor = float(input('número: '))
    if valor < 0:
        break
    else:
        numeros.append(valor)
print(f'o maior valor lido foi {max(numeros)} e o menor foi {min(numeros)}')
