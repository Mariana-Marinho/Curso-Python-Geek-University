"""
Primeiro múltiplo de 11, 13 ou 17 a partir de um número lido
"""
while True:
    try:
        numero = int(input('digite um número: '))
        break
    except Exception as erro:
        print(f'ERROR: {erro}')
i = numero
c = mul_11 = mul_13 = mul_17 = 0
while True:
    if i % 11 == 0 and mul_11 == 0:
        mul_11 = i
    elif i % 13 == 0 and mul_13 == 0:
        mul_13 = i
    elif i % 17 == 0 and mul_17 == 0:
        mul_17 = i
    if mul_11 != 0 and mul_13 != 0 and mul_17 != 0:
        break
    i += 1
print(f'o primeiro múltiplo de 11 é {mul_11}')
print(f'o primeiro múltiplo de 13 é {mul_13}')
print(f'o primeiro múltiplo de 17 é {mul_17}')
