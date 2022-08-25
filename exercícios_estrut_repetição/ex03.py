"""
Contagem regressiva
"""
from time import sleep

seg = 10
while seg > 0:
    print(seg, end='...')
    seg -= 1
    sleep(1)
print('\nFIM!')
