"""
Somar valores digitados pelo usuário
"""
quant = int(input('quantos valores deseja somar? '))
soma = 0
for c in range(0, quant):
    num = float(input(f'digite o {c+1}º número: '))
    soma += num
print(f'a soma foi igual a {soma}')
