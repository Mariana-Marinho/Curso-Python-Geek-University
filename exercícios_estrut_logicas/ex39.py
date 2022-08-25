"""
Faça um programa que calcule o retorno de um investimento com juros compostos
"""
saldo = mes = 0
c = 1
investir = float(input('quanto você investe por mês? '))
taxa = float(input('qual a taxa de juros mensal? '))/100
while True:
    mes += 12
    for t in range(0, mes):
        saldo += investir * (1+taxa)**t
    print(f'o saldo de {c} anos foi igual a {saldo:8.2f} reais')
    e = input('deseja calcular o próximo ano? [S/N] ').upper().strip()[0]
    if e == 'N':
        break
    else:
        c += 1
