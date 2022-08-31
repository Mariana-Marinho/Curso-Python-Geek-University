"""
Calcular número harmônico de n
"""
while True:
    try:
        numero = int(input('digite um número: '))
        if numero >= 1:
            break
    except Exception as erro:
        print(f'ERROR: {erro}')
harmonico = 0
for divisor in range(1, numero+1):
    harmonico += 1/divisor
print(f'o número harmônico de {numero} vale {harmonico:.4f}')
