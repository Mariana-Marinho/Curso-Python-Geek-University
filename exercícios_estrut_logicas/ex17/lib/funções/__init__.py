"""
Operações matemáticas
"""
from exercícios_estrut_logicas.ex17.lib.interface import *


def somar(quantidade):
    soma = 0
    for i in range(1, quantidade+1):
        valor = ler_numero_qualquer(f'digite o {i}º número: ')
        soma += valor
    print(f'a soma dos valore deu: {soma}')


def subtrair(quantidade):
    resto = 0
    numeros = []
    for i in range(1, quantidade+1):
        numeros.append(ler_numero_qualquer(f'digite o {i}º número: '))
    for i, v in enumerate(numeros):
        if i == 0:
            resto = v
            print(f'{v}', end='')
        else:
            resto -= v
            print(f'-{v}', end='')
    print(f' = {resto}')


def multiplicar():
    numero_1 = ler_numero_qualquer('digite o primeiro número: ')
    numero_2 = ler_numero_qualquer('digite o segundo número: ')
    produto = numero_1*numero_2
    print(f'{numero_1}*{numero_2} = {produto}')


def dividir():
    numero_1 = ler_numero_qualquer('digite o primeiro número: ')
    numero_2 = ler_numero_qualquer('digite o segundo número: ')
    quociente = numero_1/numero_2
    print(f'{numero_1}/{numero_2} = {quociente}')