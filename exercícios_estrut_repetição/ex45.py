"""
Converter de k/h para m/s e vice versa
"""
print(f'{"MENU":^15}')
print('[1]- m/s para km/h')
print('[2]- km/h para m/s')
escolha = int(input('sua escolha: '))
if escolha == 1 or escolha == 2:
    if escolha == 1:
        velocidade = float(input('velocidade em m/s: '))
        nova_velocidade = 3.6 * velocidade
        print(f'{velocidade} m/s = {nova_velocidade} km/h')
    else:
        velocidade = float(input('velocidade em km/h: '))
        nova_velocidade = velocidade/3.6
        print(f'{velocidade} km/h = {nova_velocidade} m/s')
else:
    print('PROGRAMA FINALIZADO')
