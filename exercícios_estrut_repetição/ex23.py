"""
Ler um inteiro e imprimir seus divisores
"""
while True:
    try:
        num = int(input('digite um inteiro: '))
        break
    except Exception as erro:
        print(f'ERROR: {erro}')
print(f'divisores do número {num}: ', end='')
for divisor in range(1, num+1):
    if num % divisor == 0:
        print(divisor, end='...')
