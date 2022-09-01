"""
Calcular o valor de S
S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50
"""
divisor = 1
S = 0
for dividendo in range(1, 100, 2):
    S += dividendo/divisor
    divisor += 1
print(f'o valor e S = {S}')
