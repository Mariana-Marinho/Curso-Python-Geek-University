"""
Retornar quantidade de notas de um saque num caixa eletrônico
"""
saque = int(input('sacando quantos reais? '))
for ced in (100, 50, 20, 10, 5, 2, 1):
    cedulas = saque // ced
    if cedulas != 0:
        print(f'{cedulas} cédulas de {ced} reais')
    saque %= ced
    if saque == 0:
        break
