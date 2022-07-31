"""
Dividir o valor do prêmio de 780_000 entre 3 ganhadores:
    o primeiro ganhador receberá 46%
    o segundo receberá 32%
    o terceiro receberá o restante
"""
primeiro = input('digite o nome do ganhador: ')
segundo = input('digite o nome do 2o lugar: ')
terceiro = input('digite o nome do 3o colocado: ')
valor1 = 780_000*0.46
valor2 = 780_000*0.32
valor3 = 780_000-valor2-valor1
print(f'{primeiro} receberá {valor1:.2f}\n{segundo} receberá {valor2:.2f}\n{terceiro} receberá {valor3:.2f}')
