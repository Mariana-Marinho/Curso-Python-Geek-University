"""
Menu com 4 opções operações matemáticas básicas
"""
from exercícios_estrut_logicas.ex17.lib.funções import *

while True:
    escolha = menu(['somar', 'subtrair', 'multiplicar', 'dividir', 'sair'])
    if escolha == 1:
        while True:
            numeros = ler_numero_positivo('\nquantos números deseja somar? ')
            if numeros > 1:
                break
            else:
                print('só se pode somar 2 ou mais valores')
        somar(numeros)
    if escolha == 2:
        while True:
            numeros = ler_numero_positivo('\nquantos números deseja subtrair? ')
            if numeros > 1:
                break
            else:
                print('só se pode subtrair 2 ou mais valores')
        subtrair(numeros)
    if escolha == 3:
        multiplicar()
    if escolha == 4:
        dividir()
    if escolha == 5:
        print('programa finalizado')
        break
    else:
        print('digite um número entre 1 e 5')
