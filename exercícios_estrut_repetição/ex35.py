"""
Somar números ímpares dentro de um intervalo
"""
inicio = int(input('valor inicial: '))
fim = int(input('valor final: '))
if fim <= inicio:
    print('ERROR: números inválidos')
    print('PROGRAMA FINALIZADO')
else:
    soma = 0
    for num in range(inicio, fim):
        if num % 2 != 0:
            soma += num
    print(f'a soma dos ímpares nesse intervalo é igual a {soma}')
