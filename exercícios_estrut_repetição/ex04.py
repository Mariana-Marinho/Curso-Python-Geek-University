"""
Somar de 1.000 em 1.000 até dar 100.000
"""
num = 0
print(num, end='')
while num < 100_000:
    num += 1000
    print(f' + {num}', end='')
print()
print(f' = {num}')
