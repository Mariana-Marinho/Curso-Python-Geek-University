"""
Ler distância e quantidade de litros de gasolina consumidos por um carro, calcular o consumo
"""


def consumo(km, litros):
    g = km/litros
    return g


quilometros = float(input('quantos quilômetros seu carro andou? '))
gasolina = float(input(f'quantos litros foram necessário para andar {quilometros}km? '))
gasto = consumo(quilometros, gasolina)
if gasto < 8:
    print('seu carro consome muita gasolina, viu!')
elif 8 <= gasto <= 12:
    print('seu carro é econômico')
else:
    print('seu carro é muito econômico!')
