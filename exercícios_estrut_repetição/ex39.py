"""
Calcular a área de um triângulo
"""
while True:
    altura = float(input('altura do triângulo: '))
    base = float(input('base do triângulo: '))
    if altura <= 0 or base <= 0:
        print('digite valores válidos')
    else:
        area = base*altura/2
        print(f'a área do triângulo vale {area}')
        break
