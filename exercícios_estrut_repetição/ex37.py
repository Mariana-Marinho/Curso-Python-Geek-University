"""
Verificar qual número entre 1000 e 9999 que o quadrado a soma da dezena e unidade mais milhar e centena dê o número
ex: 3025
30 + 25 = 55
55² = 3025
"""
print('números que possuem tal propriedade: ')
for num in range(1000, 10000):
    menores = num % 100
    maiores = num // 100
    if (maiores+menores)**2 == num:
        print(f'{maiores} + {menores} = {maiores+menores}')
        print(f'{maiores+menores}² = {num}\n')
