"""
Calcular o valor a ser pago num lanche
"""


def comida(menu):
    codigo = {
        'Cachorro Quente': 100,
        'Bauru Simples': 101,
        'Bauru com Ovo': 102,
        'Hamburguer': 103,
        'Cheeseburguer': 104,
        'Suco': 105,
        'Refrigerante': 106
    }
    return codigo.get(menu)


def preco(cod):
    tabela = {
        100: 1.2,
        101: 1.3,
        102: 1.5,
        103: 1.2,
        104: 1.7,
        105: 2.2,
        106: 1
    }
    return tabela.get(cod)


print(''' MENU

    Cachorro Quente
    Bauru Simples
    Bauru com Ovo
    Hamburguer
    Cheeseburguer
    Suco
    Refrigerante

''')
lanche = input('digite o que você quer comer: ')
quant = i
codigo = comida(lanche)
pagar = preco(codigo)