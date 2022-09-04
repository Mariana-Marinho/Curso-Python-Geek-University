"""
Chico tem 1.5m e cresce 2cm por ano e Zé tem 1.10m e cresce 3cm por ano, quantos anos zé vai ser maior
"""
chico = 150
ze = 110
anos = 0
while True:
    chico += 2
    ze += 3
    anos += 1
    if ze > chico:
        print(f'foram {anos} anos para zé ser maior, ele está com {ze/100}m e chico está com {chico/100}m')
        break
